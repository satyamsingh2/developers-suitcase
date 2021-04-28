from happy_homes.rentals.models.owners import Owner
from rest_framework.serializers import ModelSerializer

class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'