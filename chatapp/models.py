from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    text = models.CharField('本文',max_length=200)
    touser = models.CharField('宛先',max_length=200)
    date = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.text

class Follow(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    follow = models.CharField('追加',max_length=50)

    def __str__(self):
        return self.follow
