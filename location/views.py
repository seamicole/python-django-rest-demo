# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.permissions import AllowAny

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
