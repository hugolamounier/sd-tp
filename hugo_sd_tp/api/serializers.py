from rest_framework import serializers

from .models import Artigo

class ArtigoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'descricao', 'autor', 'anoPublicacao', 'url')