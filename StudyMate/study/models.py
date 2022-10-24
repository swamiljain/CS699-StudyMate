from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic_name=models.CharField(max_length=200)


