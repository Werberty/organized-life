from django.db import models
from core.models import Base
from model_utils.models import TimeStampedModel


class Card(Base, TimeStampedModel):
    title = models.CharField(max_length=255)


class Tasks(Base, TimeStampedModel):
    time_init = models.DateTimeField(auto_now_add=True)
    phase = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
