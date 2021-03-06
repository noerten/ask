from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
  title = models.CharField(max_length = 255)
  text = models.TextField()
  added_at = models.DateTimeField(default = timezone.now)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, related_name='question_user')
  likes = models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add = True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
