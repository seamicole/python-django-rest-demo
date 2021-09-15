# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import requests

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db import transaction
from django.utils import timezone

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from config.celery import app

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ FETCH EXCHANGE RATES
# └─────────────────────────────────────────────────────────────────────────────────────


@app.task(name="fetch-exchange-rates")
def fetch_exchange_rates():
    """ Fetches USD exchange rates for each Currency object """

    # Define API url
    url = "https://api.exchangerate.host/latest?base=USD"

    # Make request to exchange rate API
    response = requests.get(url)

    # Return if status code is not 200
    if response.status_code != 200:
        return

    # Get data from response
    data = response.json()

    # Get rates from data
    rates = data["rates"]

    # Get rates updated at timestamp
    rates_updated_at = timezone.now()

    # Get all currency codes
    currency_codes = Currency.objects.all().values_list("pk", "code")

    # Initialize atomic transaction block to reduce overhead
    with transaction.atomic():

        # Iterate over currency codes
        for pk, currency_code in currency_codes:

            # Get rate per USD
            per_usd = rates.get(currency_code)

            # Continue if rate is None
            if per_usd is None:
                continue

            # Get rate in USD
            in_usd = 1 / per_usd

            # Update currency exchange rates
            Currency.objects.filter(pk=pk).update(
                per_usd=per_usd, in_usd=in_usd, rates_updated_at=rates_updated_at
            )
