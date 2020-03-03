from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model


UserAuthor = get_user_model()

class News(models.Model):
    author = models.ForeignKey(UserAuthor,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image_file = models.FileField(upload_to='documents/news_image/',default='ADD IMAGE')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('news:detail_news',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey('news.News',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('news_list')

    def __str__(self):
        return self.text
