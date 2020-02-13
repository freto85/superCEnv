from django.contrib import admin
from .models import Document, Audio

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('description', 'document','uploaded_at')

admin.site.register(Document, DocumentAdmin)
# Register your models here.

class AudioAdmin(admin.ModelAdmin):
    list_display = ('description', 'audio_file','uploaded_at')

admin.site.register(Audio, AudioAdmin)
