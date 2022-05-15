from django.db import models

from core.models import TimeStampMixin


class Employee(TimeStampMixin):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
