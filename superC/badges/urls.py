from django.urls import path
from . import views

urlpatterns = [
    path('badges/',views.BadgesView.as_view(),name='badges'),
]
