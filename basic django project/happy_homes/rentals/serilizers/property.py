from happy_homes.rentals.models.property import Property
from rest_framework.serializers import ModelSerializer

class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'