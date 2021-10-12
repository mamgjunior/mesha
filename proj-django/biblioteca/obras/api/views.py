from rest_framework import viewsets
from ..models import Obras
from .serializers import ObrasSerializer


class ObrasViewSet(viewsets.ModelViewSet):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
