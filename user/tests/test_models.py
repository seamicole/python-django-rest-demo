# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.test import TestCase

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER MODEL TEST CASE
# └─────────────────────────────────────────────────────────────────────────────────────


class UserModelTestCase(TestCase):
    """ User Model Test Case """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST STRING METHOD
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_string_method(self):
        """ Ensures that the string method behaves as expected """

        # Define email address
        email = "Markus.Lombard@gmail.com"

        # Create user
        user = User.objects.create_user(email=email, password="password")

        # Assert that the string of user is their email
        self.assertEqual(str(user), user.email)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ TEST EMAIL IS SLUGIFIED
    # └─────────────────────────────────────────────────────────────────────────────────

    def test_email_is_slugified(self):
        """ Ensures that a user's email address is always slugified """

        # Define email address
        email = "Jérémy.Dupont@GMAIL.com"

        # Define slugified email
        email_slugified = "jeremy.dupont@gmail.com"

        # Create user
        user = User.objects.create_user(email=email, password="password")

        # Assert that created user's email is slugified
        self.assertEqual(user.email, email_slugified)

        # Reset email to initial unslugified value
        user.email = email

        # Assert that the instance now has an unslugified email
        self.assertEqual(user.email, email)

        # Save user to database
        user.save()

        # Assert that the user instance's email was slugified again on save
        self.assertEqual(user.email, email_slugified)

        # Assert that this is true on the database side as well
        self.assertEqual(User.objects.filter(email=email_slugified).count(), 1)
