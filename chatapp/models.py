from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    touser = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Follow(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    follow = models.CharField(max_length=50)

    def __str__(self):
        return self.follow
