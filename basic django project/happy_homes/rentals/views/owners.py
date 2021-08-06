from happy_homes.rentals.models.owners import Owner
from happy_homes.rentals.serilizers.owners import OwnerSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from happy_homes.rentals.pagination import CommonPagination
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                            TokenAuthentication,)
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        DjangoObjectPermissions,
                                        )
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from happy_homes.rentals.throttle import JackRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from happy_homes.rentals.signals import notification, owner


class OwnerListView(ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = CommonPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["name", "mobile_number"]
    # filter_backends = [SearchFilter] # u can even change the word search in the browser
    # search_fields = ["name"] # u can make this to be exact search or approx search

    def list(self, request, *args, **kwargs):
        # this list func wasn't needed to be written because it is triggered by itself
        # but as i want to use signal thats why i am using it
        print('inside view\n')
        owner.send(sender=None, owner=1)
        print('\n')
        return super().list(request, *args, **kwargs)



"""for this we are using basic authentication for only one class"""
class OwnerDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = OwnerSerializer
    lookup_url_kwarg = "owner_id"
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny] if done this will allow anyone to access this api
    # permission_classes = [IsAdminUser]  #for user for which is staff true only they can access this api
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]  gives only readonly permission if not authenticated
    # permission_classes = [DjangoModelPermissions] gives write permission is the user is allowed at backend
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly] gives read only permission to unauthentic + feature of Django model permission
    # authentication_classes = [TokenAuthentication]
    # throttle_classes = [AnonRateThrottle] the throttle canbe applied to all project by mentioning in settings
    # throttle_classes = [UserRateThrottle]
    # throttle_classes = [JackRateThrottle]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'scope_throttle'   #in this way u can mention scope for scoped rate throttle




    def get_object(self):
        owner_id = self.kwargs.get("owner_id")
        return Owner.objects.get(id=owner_id)

    def get(self, request, *args, **kwargs):
        notification.send(sender=None) #sending signal
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

