from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new (self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question (models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    #links
    author = models.ForeignKey(User, related_name="authors_users")
    likes = models.ManyToManyField(User, related_name="likes_users")

class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True,auto_now_add=True)
    #links
    question = models.ForeignKey(Question, related_name="question_id")
    author = models.ForeignKey(User, related_name = "author_id")
