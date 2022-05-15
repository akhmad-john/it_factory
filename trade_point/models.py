from django.db import models

from core.models import TimeStampMixin
from employee.models import Employee


class TradePoint(TimeStampMixin):
    name = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
