# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from utils.test_cases import APITestCase


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY VIEW TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyViewTestCase(APITestCase):
    """ Currency View Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CURRENCY LIST VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_currency_list_view(self):
        """ Ensures that the currency list view behaves as expected """

        # Get response
        response = self.api.get("/api/currencies/", format="json")

        # Get response data
        data = response.json()

        # Assert 200 status code
        self.assertEqual(response.status_code, 200)

        # Ensure that the endpoint returns all available currencies
        self.assertEqual(data["meta"]["result_count"], Currency.objects.all().count())

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CURRENCY DETAIL VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_currency_detail_view(self):
        """ Ensures that the currency detail view behaves as expected """

        # Get US Dollar
        usd = Currency.objects.get(code="USD")

        # Get lookups
        lookups = (usd.pk, usd.code, usd.code.lower())

        # Iterate over lookups
        for lookup in lookups:

            # Get response
            response = self.api.get(f"/api/currencies/{lookup}", format="json")

            # Assert 200 status code for each lookup
            self.assertEqual(response.status_code, 200)
