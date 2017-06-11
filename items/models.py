from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Item(models.Model):
    item_title = models.CharField(max_length=200)
    item_text = models.CharField(max_length=400)
    item_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.item_title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Question(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_answer = models.CharField(max_length=400, default='')
    answered = models.BooleanField(default=False)
    def __str__(self):
        return self.question_text
