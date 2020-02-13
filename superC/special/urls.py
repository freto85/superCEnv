from django.urls import path
from . import views

urlpatterns = [
    path('special/',views.SpecialPage.as_view(),name='special'),
]
