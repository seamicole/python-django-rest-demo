# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from location.serializers import CountrySerializer


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY SERIALIZER
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencySerializer(DynamicModelSerializer):

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define upward foreign key fields
    country = DynamicRelationField(CountrySerializer)

    # Define downward foreign key fields
    countries = DynamicRelationField(CountrySerializer, many=True, deferred=True)

    # Ensure that flag falls back to country flag
    flag = serializers.ImageField(source="flag_or_country_flag")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:
        """ Meta Class """

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ MODEL
        # └─────────────────────────────────────────────────────────────────────────────

        model = Currency
        name = "currency"

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ FIELDS
        # └─────────────────────────────────────────────────────────────────────────────

        fields = (
            "id",
            "country",
            "name",
            "name_plural",
            "code",
            "number",
            "symbol",
            "symbol_native",
            "in_usd",
            "per_usd",
            "rates_updated_at",
            "flag",
            "countries",
        )
