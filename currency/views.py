# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db.models import Q

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from currency.serializers import CurrencySerializer
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
    # │ RETRIEVE
    # └─────────────────────────────────────────────────────────────────────────────────

    def retrieve(self, request, pk=None):
        """ Custom Retrieve Method """

        # Check if pk is alpha string
        if pk and pk.isalpha():

            # Uppercase pk
            pk = pk.upper()

            # Get currency whose code matches pk
            currency = self.get_queryset().filter(Q(code=pk) | Q(code=pk)).first()

            # Check if currency exists
            if currency:

                # Get currency serializer
                serializer = self.get_serializer(currency)

                # Return serialized data
                return Response(serializer.data)

        # Return parent method
        return super().retrieve(request, pk=pk)
