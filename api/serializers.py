from core.models import Comunidad, Boda, Bautizo, Comunion
from rest_framework import serializers
#Serializacion
class ComunidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields= ('id', 'nombre')

class BodaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Boda
        fields = ('id', 'nombreNovia', 'nombreNovio', 'numeroContacto', 'emailContacto', 'tipoParroquia')

class BautizoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bautizo
        fields = ('id', 'bautizado', 'edad', 'padrino', 'madrina', 'tipoParroquia')

class ComunionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunion
        fields = ('id', 'nombreComunion', 'edad', 'numeroContacto', 'emailContacto', 'direccion', 'tipoParroquia')
