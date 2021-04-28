from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from happy_homes.rentals.pagination import CommonPagination
from happy_homes.rentals.models.people import People
from happy_homes.rentals.serilizers.people import PeopleSerializer


class PeopleListView(ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    pagination_class = CommonPagination


class PeopleDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = PeopleSerializer
    lookup_url_kwarg = "people_id"

    def get_object(self):
        people_id = self.kwargs.get("people_id")
        return People.objects.get(id=people_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
