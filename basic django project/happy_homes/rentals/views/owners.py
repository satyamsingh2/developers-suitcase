from happy_homes.rentals.models.owners import Owner
from happy_homes.rentals.serilizers.owners import OwnerSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from happy_homes.rentals.pagination import CommonPagination


class OwnerListView(ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = CommonPagination


class OwnerDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = OwnerSerializer
    lookup_url_kwarg = "owner_id"

    def get_object(self):
        owner_id = self.kwargs.get("owner_id")
        return Owner.objects.get(id=owner_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

