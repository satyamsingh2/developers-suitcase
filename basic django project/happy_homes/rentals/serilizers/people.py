from happy_homes.rentals.models.people import People
from rest_framework.serializers import ModelSerializer

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'