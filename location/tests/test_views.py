# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.models import Currency
from location.models import City, Country
from utils.test_cases import APITestCase


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY VIEW TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CityViewTestCase(APITestCase):
    """ City View Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CITY LIST VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_city_list_view(self):
        """ Ensures that the city list view behaves as expected """

        # Get response
        response = self.api.get("/api/cities/", format="json")

        # Get response data
        data = response.json()

        # Assert 200 status code
        self.assertEqual(response.status_code, 200)

        # Ensure that the endpoint returns all available cities
        self.assertEqual(data["meta"]["result_count"], City.objects.all().count())

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CITY DETAIL VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_city_detail_view(self):
        """ Ensures that the city detail view behaves as expected """

        # Get Bangkok
        bangkok = Country.objects.get(iso3="THA").capital

        # Get response
        response = self.api.get(f"/api/cities/{bangkok.pk}", format="json")

        # Assert 200 status code for each lookup
        self.assertEqual(response.status_code, 200)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY VIEW TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryViewTestCase(APITestCase):
    """ Country View Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST COUNTRY LIST VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_country_list_view(self):
        """ Ensures that the country list view behaves as expected """

        # Get response
        response = self.api.get("/api/countries/", format="json")

        # Get response data
        data = response.json()

        # Assert 200 status code
        self.assertEqual(response.status_code, 200)

        # Ensure that the endpoint returns all available countries
        self.assertEqual(data["meta"]["result_count"], Country.objects.all().count())

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST COUNTRY DETAIL VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_country_detail_view(self):
        """ Ensures that the country detail view behaves as expected """

        # Get Thailand
        tha = Country.objects.get(iso3="THA")

        # Get lookups
        lookups = (tha.pk, tha.iso2, tha.iso2.lower(), tha.iso3, tha.iso3.lower())

        # Iterate over lookups
        for lookup in lookups:

            # Get response
            response = self.api.get(f"/api/countries/{lookup}", format="json")

            # Assert 200 status code for each lookup
            self.assertEqual(response.status_code, 200)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY OF COUNTRY VIEW TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CityOfCountryViewTestCase(APITestCase):
    """ City Of Country View Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CITY OF COUNTRY LIST VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_city_of_country_list_view(self):
        """ Ensures that the city of country list view behaves as expected """

        # Get Thailand
        tha = Country.objects.get(iso3="THA")

        # Get lookups
        lookups = (tha.pk, tha.iso2, tha.iso2.lower(), tha.iso3, tha.iso3.lower())

        # Iterate over lookups
        for lookup in lookups:

            # Get response
            response = self.api.get(f"/api/countries/{lookup}/cities", format="json")

            # Get response data
            data = response.json()

            # Assert 200 status code for each lookup
            self.assertEqual(response.status_code, 200)

            # Ensure that the endpoint returns all available countries
            self.assertEqual(
                data["meta"]["result_count"],
                City.objects.filter(country=tha).count(),
            )


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY OF CURRENCY VIEW TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryOfCurrencyViewTestCase(APITestCase):
    """ Country Of Currency View Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST COUNTRY OF CURRENCY LIST VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_country_of_currency_list_view(self):
        """ Ensures that the country of currency list view behaves as expected """

        # Get US Dollar
        usd = Currency.objects.get(code="USD")

        # Get lookups
        lookups = (usd.pk, usd.code, usd.code.lower())

        # Iterate over lookups
        for lookup in lookups:

            # Get response
            response = self.api.get(
                f"/api/currencies/{lookup}/countries", format="json"
            )

            # Get response data
            data = response.json()

            # Assert 200 status code for each lookup
            self.assertEqual(response.status_code, 200)

            # Ensure that the endpoint returns all available countries
            self.assertEqual(
                data["meta"]["result_count"],
                Country.objects.filter(currency=usd).count(),
            )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST COUNTRY OF CURRENCY DETAIL VIEW
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_country_of_currency_detail_view(self):
        """ Ensures that the country of currency detail view behaves as expected """

        # Get US Dollar
        usd = Currency.objects.get(code="USD")

        # Get United States
        usa = Country.objects.get(iso3="USA")

        # Get lookups
        lookups = (usa.pk, usa.iso2, usa.iso2.lower(), usa.iso3, usa.iso3.lower())

        # Iterate over lookups
        for lookup in lookups:

            # Get response
            response = self.api.get(
                f"/api/currencies/{usd.pk}/countries/{lookup}/", format="json"
            )

            # Assert 200 status code for each lookup
            self.assertEqual(response.status_code, 200)
