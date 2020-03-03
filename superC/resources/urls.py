from django.urls import path
from . import views

urlpatterns = [
    path('homework/',views.ActivitiesView.as_view(),name='homework'),
    path('library/',views.DownloadsView.as_view(),name='library'),
    path('games/',views.GamesView.as_view(),name='games'),
    path('glossary/',views.GlossaryView.as_view(),name='glossary'),
    path('media/',views.display_media,name='media'),
    path('media/video/create/',views.UploadVideoView.as_view(),name='upload_video'),
    path('media/video/<int:pk>/',views.VideoDetailView.as_view(),name='detail_video'),
    path('media/video/<int:pk>/remove/',views.VideoDeleteView.as_view(),name='delete_video'),
    path('media/audio/create/',views.audio_upload,name='upload_audio'),
    path('media/audio/<int:pk>/',views.AudioDetailView.as_view(),name='detail_audio'),
    path('media/audio/<int:pk>/remove/',views.AudioDeleteView.as_view(),name='delete_audio'),
    path('media/image/create/',views.image_upload,name='upload_image'),
    path('media/image/<int:pk>/',views.ImageDetailView.as_view(),name='detail_image'),
    path('media/image/<int:pk>/remove/',views.ImageDeleteView.as_view(),name='delete_image'),
]
