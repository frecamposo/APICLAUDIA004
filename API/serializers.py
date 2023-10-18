from .models import Receta,Repartidor
from rest_framework import serializers

class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"

class RepartidorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Repartidor
        fields = "__all__"
