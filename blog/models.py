from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Commnet(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=50,default='Stranger')
    comment_text = models.TextField(max_length=200)

    def __str__(self):
        return self.comment_author
    #comment_date = models.DateTimeField(blank=True, null=True)

