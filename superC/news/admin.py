from django.contrib import admin
from news.models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('author','title','text','image_file')

admin.site.register(News, NewsAdmin)
