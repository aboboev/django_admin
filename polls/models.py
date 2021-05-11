from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    pub_time = models.TimeField('time_published')
    extra_text = models.CharField(max_length=250)
