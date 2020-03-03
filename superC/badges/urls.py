from django.urls import path
from . import views

urlpatterns = [
    path('',views.BadgesView.as_view(),name='badges'),
]
