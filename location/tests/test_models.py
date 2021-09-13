# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from location.models import Country


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY MODEL TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CityModelTestCase(TestCase):
    """ City Model Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STRING METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_string_method(self):
        """ Ensures that the string method behaves as expected """

        # Get Bangkok
        bangkok = Country.objects.get(iso3="THA").capital

        # Assert that the string of a city is its name
        self.assertEqual(str(bangkok), bangkok.name)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY MODEL TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryModelTestCase(TestCase):
    """ Country Model Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STRING METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_string_method(self):
        """ Ensures that the string method behaves as expected """

        # Get Thailand
        thailand = Country.objects.get(iso3="THA")

        # Assert that the string of a city is its name
        self.assertEqual(str(thailand), thailand.name)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST CAPITAL UNICITY
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_capital_unicity(self):
        """ Ensures that a capital can only belong to one country """

        # Get Bangkok
        bangkok = Country.objects.get(iso3="THA").capital

        # Get United States
        united_states = Country.objects.get(iso3="USA")

        # Initialize assertRaises block
        with self.assertRaises(IntegrityError):

            # Set the capital of United States to Bangkok
            united_states.capital = bangkok

            # Try to save United States object to database
            united_states.save()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST UN MEMBER STATUS
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_un_member_status(self):
        """ Ensures that the cleaning of UN member status behaves as expected """

        # Get Hong Kong
        hong_kong = Country.objects.get(iso3="HKG")

        # Assert that is_un_member_at is None
        self.assertEqual(hong_kong.is_un_member_at, None)

        # Initialize assertRaises block
        with self.assertRaises(ValidationError):

            # Set is UN member to True
            hong_kong.is_un_member = True

            # Attempt to clean the Hong Kong object
            hong_kong.clean()

            # Should fail because no corresponding is UN member at date is set

        # Get Thailand
        thailand = Country.objects.get(iso3="THA")

        # Assert that Thailand is a UN member state
        self.assertEqual(thailand.is_un_member, True)

        # Assert that Thailand is UN member at is not None
        self.assertIsNotNone(thailand.is_un_member_at)

        # Set Thailand is UN member at to False
        thailand.is_un_member = False

        # Clean Thailand object
        thailand.clean()

        # Asser that Thailand is UN member at is now None
        self.assertIsNone(thailand.is_un_member_at)
