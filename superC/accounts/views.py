from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, TemplateView,DetailView,ListView,UpdateView)
from accounts.forms import (UserCreateForm, AccountUpdatePersonalInfoForm,
                            AccountUpdateMedalsForm, AccountUpdateTrophiesForm,
                            AccountUpdateStickersForm, AccountUpdateRoadmapForm, MessageForm,NewMessageForm)
from accounts.models import User, MyAccountManager, Message
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

user_filter = get_user_model()
# Create your views here.

class AccountView(TemplateView):
    template_name = 'accounts/account_info.html'

class AccountDetailView(DetailView,LoginRequiredMixin):
    template_name = 'accounts/account_detail.html'
    model = User

class AccountListView(ListView, LoginRequiredMixin):
    model = User
    template_name = 'accounts/account_list.html'

class AccountUpdatePersonalView(UpdateView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'accounts/account_update_personal.html'
    redirect_field_name = 'accounts:detail_account'
    form_class = AccountUpdatePersonalInfoForm
    model = User

class AccountUpdateMedalsView(UpdateView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'accounts/account_update_medals.html'
    redirect_field_name = 'accounts:detail_account'
    form_class = AccountUpdateMedalsForm
    model = User

class AccountUpdateTrophiesView(UpdateView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'accounts/account_update_personal.html'
    redirect_field_name = 'accounts:detail_account'
    form_class = AccountUpdateTrophiesForm
    model = User

class AccountUpdateStickersView(UpdateView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'accounts/account_update_personal.html'
    redirect_field_name = 'accounts:detail_account'
    form_class = AccountUpdateStickersForm
    model = User

class AccountUpdateRoadmapView(UpdateView, LoginRequiredMixin):
    login_url = '/accounts/login/'
    template_name = 'accounts/account_update_roadmap.html'
    redirect_field_name = 'accounts:detail_account'
    form_class = AccountUpdateRoadmapForm
    model = User


class MessagesView(TemplateView):
    template_name = 'accounts/messages.html'


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def messages_list(request):
    username = request.user.pk
    messages = Message.objects.filter(Q(sender=username) | Q(receiver=username)).order_by('-created_at')
    list = []
    user_list = []
    for e in messages:
        list.append(e.sender)
        list.append(e.receiver)
    list= set(list)
    for e in list:
        user_list.append(User.objects.get(id=e.pk).id)
    sorted(user_list)
    template_name = 'accounts/messages_list.html'
    context = {'list': list}
    return render (request, 'accounts/messages_list.html', context)


def messages_content(request,pk):
    template_name = 'accounts/messages_content.html'
    receiver = pk
    user_instance = request.user
    username = request.user.pk
    other_person = User.objects.get(id=receiver)
    messages = Message.objects.filter((Q(sender=username) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=username))).order_by('created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_form = form.save(commit=False)
            message_form.save()
            new_message = Message(sender=user_instance,receiver=other_person, message_dataID=message_form)
            new_message.save()
    else:
        form = MessageForm()

    context = {'messages': messages,
                'other_person': other_person,
                'form' : form,
                'boob' : request,
                }
    return render (request, 'accounts/messages_content.html', context)

def messages_new(request):
    username = request.user
    if request.method == 'POST':
        form_user = NewMessageForm(request.POST)
        form_message = MessageForm(request.POST)
        if form_user.is_valid() and form_message.is_valid():
            message = form_message.save()
            instance = form_user.save()
            instance.sender = username
            instance.message_dataID = message
            instance.save()
            return redirect('accounts:messages_list')
    else:
        form_user = NewMessageForm()
        form_message = MessageForm()
    context = {'form_user': form_user,
                'form_message': form_message,
                }
    return render (request, 'accounts/new_message.html', context)


#def messages_content_list(request):
#    current_message = get_object_or_404
#    messages = Message.objects.filter(Q(sender=username) | Q(receiver=username)).order_by('-created_at')

#    model = Message
#    template_name = 'accounts/messages_list.html'


# def messages_list_content(request):

#    messages = Message.objects.filter(Q(sender=username) | Q(receiver=username)).order_by('-created_at')
#     context = {'messages': messages }
