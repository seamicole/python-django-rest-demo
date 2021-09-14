# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db.models import Q

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from location.models import City, Country
from location.serializers import CitySerializer, CountrySerializer
from utils.pagination import DynamicPagination
from utils.viewsets import DynamicReadOnlyModelViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CityViewSet(DynamicReadOnlyModelViewSet):

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define model
    model = City

    # Define serializer class
    serializer_class = CitySerializer

    # Define pagination class
    pagination_class = DynamicPagination

    # Define permission classes
    permission_classes = [AllowAny]

    # Define search fields
    search_fields = ["name"]

    # Define queryset
    queryset = City.objects.all().select_related("country").order_by("name")


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryViewSet(DynamicReadOnlyModelViewSet):

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define model
    model = Country

    # Define serializer class
    serializer_class = CountrySerializer

    # Define pagination class
    pagination_class = DynamicPagination

    # Define permission classes
    permission_classes = [AllowAny]

    # Define search fields
    search_fields = ["name", "name_native"]

    # Define queryset
    queryset = Country.objects.all().prefetch_related("cities").order_by("name")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ RETRIEVE
    # └─────────────────────────────────────────────────────────────────────────────────

    def retrieve(self, request, pk=None):
        """ Custom Retrieve Method """

        # Check if pk is alpha string
        if pk and pk.isalpha():

            # Uppercase pk value
            pk = pk.upper()

            # Get country whose ISO code matches pk
            country = self.get_queryset().filter(Q(iso2=pk) | Q(iso3=pk)).first()

            # Check if country exists
            if country:

                # Get country serializer
                serializer = self.get_serializer(country)

                # Return serialized data
                return Response(serializer.data)

        # Return parent method
        return super().retrieve(request, pk=pk)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY OF COUNTRY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CityOfCountryViewSet(CityViewSet):

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET QUERYSET
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_queryset(self):
        """ Returns a queryset of cities filtered by a given country """

        # Get country primary key
        country_pk = self.kwargs.get("country_pk")

        # Get country
        country = get_object_or_404(Country.objects.all(), pk=country_pk)

        # Get queryset
        queryset = City.objects.filter(country=country)

        # Return queryset
        return queryset
