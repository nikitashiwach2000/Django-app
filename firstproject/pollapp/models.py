from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class questions(models.Model):

    question_test = models.CharField(max_length=200)
    date = models.DateTimeField('date Published')
    def __str__(self):
        return self.question_test

    @admin.display(boolean=True, ordering='date', description='Published recently?',)
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
        # return self.date <= timezone.now() - datetime.timedelta(days=1)
    
class choice(models.Model):
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
print("models")

