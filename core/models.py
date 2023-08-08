from django.db import models
import uuid


class Base(models.Model):  # order is important
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)