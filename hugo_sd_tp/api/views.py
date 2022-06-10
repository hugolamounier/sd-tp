from rest_framework import viewsets

from .serializers import ArtigoSerializer
from .models import Artigo
from django.db.models import Q


class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all().order_by('titulo')
    serializer_class = ArtigoSerializer

    def get_queryset(self):
        queryset = Artigo.objects.all().order_by('titulo')
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(Q(titulo__icontains=search) | Q(autor__icontains=search) | Q(descricao__icontains=search))
        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


