from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from happy_homes.rentals.pagination import CommonPagination
from happy_homes.rentals.models.membership import Membership
from happy_homes.rentals.serilizers.membership import MembershipSerializer


class MembershipListView(ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    pagination_class = CommonPagination


class MembershipDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = MembershipSerializer
    lookup_url_kwarg = "membership_id"

    def get_object(self):
        membership_id = self.kwargs.get("membership_id")
        return Membership.objects.get(id=membership_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
