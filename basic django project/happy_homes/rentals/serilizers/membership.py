from happy_homes.rentals.models.membership import Membership
from rest_framework.serializers import ModelSerializer

class MembershipSerializer(ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'