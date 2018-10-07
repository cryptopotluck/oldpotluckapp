from django.db import models
from django.contrib.auth.models import User
from blog.models import User
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=50)
    url = models.TextField()
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='upvote_author', on_delete=models.CASCADE)
    sub_feed = models.CharField(max_length=20)
    Main_Pair = models.CharField(max_length=4)
    Altcoin = models.CharField(max_length=5)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title