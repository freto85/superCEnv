from django.urls import path
from . import views

urlpatterns = [
    path('',views.NewsListView.as_view(),name='news_list'),
    path('<int:pk>/',views.NewsDetailView.as_view(),name='detail_news'),
    path('create/',views.CreateNewsView.as_view(),name='create_news'),
    path('<int:pk>/edit/',views.NewsUpdateView.as_view(),name='edit_news'),
    path('<int:pk>/remove/',views.NewsDeleteView.as_view(),name='remove_news'),
    path('drafts/',views.DraftListView.as_view(),name='draft_news'),
    path('<int:pk>/comment/',views.add_comment_to_news,name='add_comment_to_news'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('<int:pk>/publish/',views.news_publish,name='news_publish'),
]
