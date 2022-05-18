from rest_framework import viewsets

from .serializers import ArtigoSerializer
from .models import Artigo


class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all().order_by('titulo')
    serializer_class = ArtigoSerializer