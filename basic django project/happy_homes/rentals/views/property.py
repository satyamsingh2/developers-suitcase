from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from happy_homes.rentals.pagination import CommonPagination
from happy_homes.rentals.models.property import Property
from happy_homes.rentals.serilizers.property import PropertySerializer


class PropertyListView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = CommonPagination


class PropertyDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = PropertySerializer
    lookup_url_kwarg = "property_id"

    def get_object(self):
        property_id = self.kwargs.get("property_id")
        return Property.objects.get(id=property_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
