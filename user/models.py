# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from tools import slugify


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER MANAGER
# └─────────────────────────────────────────────────────────────────────────────────────


class UserManager(BaseUserManager):
    """ User Manager """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Enable this manager for migrations
    use_in_migrations = True

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE USER
    # └─────────────────────────────────────────────────────────────────────────────────

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a regular user given an email and password """

        # Check if email is null
        if not email:

            # Raise ValueError
            raise ValueError("An email address is required")

        # Normalize the email address
        email = self.normalize_email(email)

        # Create user instance
        user = self.model(email=email, **extra_fields)

        # Set user password
        user.set_password(password)

        # Save user to database
        user.save(using=self._db)

        # Return user instance
        return user

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CREATE SUPERUSER
    # └─────────────────────────────────────────────────────────────────────────────────

    def create_superuser(self, email, password, **extra_fields):
        """ Creates and saves a superuser given an email and password """

        # Create a new user
        user = self.create_user(email, password, **extra_fields)

        # Ensure that user is staff and superuser
        user.is_staff = user.is_superuser = True

        # Save user to database
        user.save(using=self._db)

        # Return user instance
        return user

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET BY NATURAL KEY
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_by_natural_key(self, email):
        """ Ensures that email is case insensitive when authenticating """

        # Get by case-insensitive email
        return self.get(email__iexact=email)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER
# └─────────────────────────────────────────────────────────────────────────────────────


class User(AbstractUser):
    """ User Model """

    # ┌────────────────────────────────────────────────────────────────────────────────┐
    # │ EMAIL                                                                          │
    # └────────────────────────────────────────────────────────────────────────────────┘

    # Nullify original username field
    username = None

    # Define email field
    email = models.EmailField(max_length=255, unique=True)

    # Set username field to email
    USERNAME_FIELD = "email"

    # Make first name required
    REQUIRED_FIELDS = ["first_name"]

    # ┌────────────────────────────────────────────────────────────────────────────────┐
    # │ MODEL MANAGER                                                                  │
    # └────────────────────────────────────────────────────────────────────────────────┘

    # Use the custom model manager
    objects = UserManager()

    # ┌────────────────────────────────────────────────────────────────────────────────┐
    # │ META                                                                           │
    # └────────────────────────────────────────────────────────────────────────────────┘

    class Meta:
        """ Meta Class """

        # Define verbose names
        verbose_name = "User"
        verbose_name_plural = "Users"

    # ┌────────────────────────────────────────────────────────────────────────────────┐
    # │ STRING METHOD                                                                  │
    # └────────────────────────────────────────────────────────────────────────────────┘

    def __str__(self):
        """ Custom String Method """

        # Return email
        return self.email

    # ┌────────────────────────────────────────────────────────────────────────────────┐
    # │ SAVE                                                                           │
    # └────────────────────────────────────────────────────────────────────────────────┘

    def save(self, *args, **kwargs):
        """ Custom Save Method """

        # Slugify the email address (case insensitive, no special characters)
        self.email = slugify(self.email, decode=True)

        # Save object
        return super().save(*args, **kwargs)
