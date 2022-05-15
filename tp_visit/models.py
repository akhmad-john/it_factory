from django.db import models

from core.models import TimeStampMixin
from trade_point.models import TradePoint


class Visit(TimeStampMixin):
    trade_point_id = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.trade_point_id.name, self.created_at)
