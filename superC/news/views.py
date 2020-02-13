from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import News, Comment
from django.urls import reverse_lazy
from news.forms import NewsForm, CommentForm

class NewsListView(ListView):
    model = News

    def get_queryset(self):
        return News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NewsDetailView(DetailView):
    model = News

class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'news:draft_news'
    form_class = NewsForm
    model = News

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    template_name_suffix = '_update_form'
    redirect_field_name = 'news:detail_news'
    form_class = NewsForm
    model = News

class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    success_url = reverse_lazy('news:news_list')

class DraftListView(LoginRequiredMixin,ListView):
    template_name = 'news/news_draft_list.html'
    model = News
    login_url = '/accounts/login/'
    redirect_field_name = 'news:news_list'


    def get_queryset(self):
        return News.objects.filter (published_date__isnull=True).order_by('created_date')

#############################################################################
############################################################################

@login_required
def news_publish(request,pk):
    news=get_object_or_404(News,pk=pk)
    news.publish()
    return redirect('news:detail_news',pk=pk)

@login_required
def add_comment_to_news(request,pk):
    news = get_object_or_404(News,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news:detail_news',pk=news.pk)
    else:
        form = CommentForm()
    return render(request,'news/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('news:detail_news', pk=comment.news.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    news_pk = comment.news.pk
    comment.delete()
    return redirect('news:detail_news',pk=news_pk)

def mysampleview(request):
    ...
    current_user_id = request.user.id
    context['current_user_id'] = current_user_id
