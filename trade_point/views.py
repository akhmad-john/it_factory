from rest_framework import generics
from rest_framework.response import Response

from .models import TradePoint
from .serializers import TradePointSerializer


class TradePointListView(generics.ListAPIView):
    lookup_url_kwarg = 'phone_number'
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer

    def list(self, request, *args, **kwargs):
        trade_points = TradePoint.objects.filter(
            employee_id__phone_number=self.kwargs.get(self.lookup_url_kwarg)
        )
        serializer = self.get_serializer(trade_points, many=True)
        return Response(serializer.data)
