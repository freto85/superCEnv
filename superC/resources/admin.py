from django.contrib import admin
from .models import MediaVideoModel, MediaImageModel, MediaAudioModel
from embed_video.admin import AdminVideoMixin

class MediaVideoModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('user','description','video_file','slug')

class MediaImageModelAdmin(admin.ModelAdmin):
    list_display = ('user','description', 'image_file','uploaded_at')

class MediaAudioModelAdmin(admin.ModelAdmin):
    list_display = ('user','description', 'audio_file','uploaded_at')

admin.site.register(MediaVideoModel, MediaVideoModelAdmin)

admin.site.register(MediaImageModel, MediaImageModelAdmin)

admin.site.register(MediaAudioModel, MediaAudioModelAdmin)
