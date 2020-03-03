from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'homepage.html'

#    def get(self, request, *args, **kwargs):
#        if request.user.is_authenticated:
#            return HttpResponseRedirect(reverse("test"))
#        return super().get(request, *args, **kwargs)
