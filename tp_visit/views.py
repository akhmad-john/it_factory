from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import VisitCreateSerializer


class VisitCreateView(generics.CreateAPIView):
    lookup_url_kwarg = 'phone_number'
    serializer_class = VisitCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trade_point = serializer.validated_data.get('trade_point_id')

        if trade_point.employee_id.phone_number != str(self.kwargs.get(self.lookup_url_kwarg)):
            return Response({
                "message": "This trade point does not belong to this employee"
            }, status=status.HTTP_403_FORBIDDEN)
        self.perform_create(serializer)
        return Response({
            "id": serializer.data.get('id'),
            "created_at": serializer.data.get('created_at')
        })
