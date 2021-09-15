# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.test import TestCase

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY MODEL TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CurrencyModelTestCase(TestCase):
    """ Currency Model Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STRING METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_string_method(self):
        """ Ensures that the string method behaves as expected """

        # Get US Dollar
        usd = Currency.objects.get(code="USD")

        # Assert that the string of a currency is its name
        self.assertEqual(str(usd), usd.name)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST FLAG OR COUNTRY FLAG PROPERTY
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_flag_or_country_flag_property(self):
        """ Ensures that flag falls back to country flag if null """

        # Get Euro
        eur = Currency.objects.get(code="EUR")

        # Assert that Euro has its own flag
        self.assertEqual(eur.flag_or_country_flag, eur.flag)

        # Get US Dollar
        usd = Currency.objects.get(code="USD")

        # Assert that US dollar uses the United States flag
        self.assertEqual(usd.flag_or_country_flag, usd.country.flag)
