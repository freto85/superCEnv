from django.urls import path
from . import views

urlpatterns = [
    path('',views.RewardsView.as_view(),name='rewards'),
    path('rewardstree/',views.RoadmapView.as_view(),name='roadmap'),
]
