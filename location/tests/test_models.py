# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.test import TestCase

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from location.models import City, Country


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ City MODEL TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class CityModelTestCase(TestCase):
    """ City Model Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STRING METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_string_method(self):
        """ Ensures that the string method behaves as expected """

        # Define email address
        email = "Markus.Lombard@gmail.com"

        # Create user
        # user = User.objects.create_user(email=email, password="password")

        # Assert that the string of user is their email
        # self.assertEqual(str(user), user.email)
