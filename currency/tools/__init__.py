# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.generics import get_object_or_404


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GET CURRENCY BY LOOKUP OR 404
# └─────────────────────────────────────────────────────────────────────────────────────


def get_currency_by_lookup_or_404(queryset, lookup, lookup_field="pk"):
    """ Returns a Currency instance based on an arbitrary string lookup """

    # Check if lookup is an alpha string
    if lookup and lookup.isalpha():

        # Uppercase lookup assuming that it is a currency code
        lookup = lookup.upper()

        # Set lookup field to code
        lookup_field = "code"

    # Get Currency instance by primary key lookup
    currency = get_object_or_404(queryset, **{lookup_field: lookup})

    # Return Currency instance
    return currency
