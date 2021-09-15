# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.permissions import AllowAny

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from currency.serializers import CurrencySerializer
from currency.tools import get_currency_by_lookup_or_404
from utils.pagination import DynamicPagination
from utils.viewsets import DynamicReadOnlyModelViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyViewSet(DynamicReadOnlyModelViewSet):
    """ Currency View Set """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define model
    model = Currency

    # Define serializer class
    serializer_class = CurrencySerializer

    # Define pagination class
    pagination_class = DynamicPagination

    # Define permission classes
    permission_classes = [AllowAny]

    # Define search fields
    search_fields = ["name", "code", "number", "country__name"]

    # Define queryset
    queryset = Currency.objects.all().select_related("country").order_by("name")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET OBJECT
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_object(self):
        """ Returns a Currency instance by currency code or primary key """

        # Get queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Get lookup URL kwarg
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # Get lookup
        lookup = self.kwargs[lookup_url_kwarg]

        # Get Currency object by lookup or 404
        obj = get_currency_by_lookup_or_404(
            queryset=queryset, lookup_field=self.lookup_field, lookup=lookup
        )

        # Chec object permissions
        self.check_object_permissions(self.request, obj)

        # Return object
        return obj
