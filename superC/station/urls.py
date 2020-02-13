from django.urls import path
from station import views


urlpatterns = [
    path('list',views.StationView.as_view(),name='station_home'),
    path('upload_file',views.model_form_upload,name='upload_file'),
    path('audio_list',views.StationAudioView.as_view(),name='station_audio_home'),
    path('upload_audio_list',views.model_form_audio_upload,name='upload_audio_file'),
]
