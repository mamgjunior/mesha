from rest_framework import generics
from ..models import Obras
from .serializers import ObrasSerializer


class ObrasListView(generics.ListAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer


class ObrasDetailView(generics.RetrieveAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
