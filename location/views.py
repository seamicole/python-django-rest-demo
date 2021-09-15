# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.permissions import AllowAny

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from currency.tools import get_currency_by_lookup_or_404
from location.models import City, Country
from location.serializers import CitySerializer, CountrySerializer
from location.tools import get_country_by_lookup_or_404
from utils.pagination import DynamicPagination
from utils.viewsets import DynamicReadOnlyModelViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CityViewSet(DynamicReadOnlyModelViewSet):
    """ City View Set """

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
    queryset = City.objects.all().order_by("name")


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryViewSet(DynamicReadOnlyModelViewSet):
    """ Country View Set """

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
    queryset = Country.objects.all().order_by("name")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET OBJECT
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_object(self):
        """ Returns a Country instance by ISO code or primary key """

        # Get queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Get lookup URL kwarg
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # Get lookup
        lookup = self.kwargs[lookup_url_kwarg]

        # Get Country object by lookup or 404
        obj = get_country_by_lookup_or_404(
            queryset=queryset, lookup_field=self.lookup_field, lookup=lookup
        )

        # Chec object permissions
        self.check_object_permissions(self.request, obj)

        # Return object
        return obj


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY OF COUNTRY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CityOfCountryViewSet(CityViewSet):
    """ City Of Country View Set """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET QUERYSET
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_queryset(self):
        """ Returns a queryset of cities filtered by a given country """

        # Get country primary key
        country_pk = self.kwargs.get("country_pk")

        # Get Country object by lookup or 404
        country = get_country_by_lookup_or_404(
            queryset=Country.objects.all(), lookup=country_pk
        )

        # Get queryset
        queryset = super().get_queryset().filter(country=country)

        # Return queryset
        return queryset


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY OF CURRENCY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryOfCurrencyViewSet(CountryViewSet):
    """ Country Of Currency View Set """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET QUERYSET
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_queryset(self):
        """ Returns a queryset of countries filtered by a given currency """

        # Get currency primary key
        currency_pk = self.kwargs.get("currency_pk")

        # Get currency object by lookup or 404
        currency = get_currency_by_lookup_or_404(
            queryset=Currency.objects.all(), lookup=currency_pk
        )

        # Get queryset
        queryset = super().get_queryset().filter(currency=currency)

        # Return queryset
        return queryset
