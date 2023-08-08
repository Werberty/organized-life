from django.db import models
from core.models import Base


class Card(Base, models.Model):
    title = models.CharField(max_length=255)


class Tasks(Base, models.Model):
    time_init = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
