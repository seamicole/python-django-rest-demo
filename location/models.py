# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.core.exceptions import ValidationError
from django.db import models


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY
# └─────────────────────────────────────────────────────────────────────────────────────


class City(models.Model):
    """ City Model """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COUNTRY
    # └─────────────────────────────────────────────────────────────────────────────────

    country = models.ForeignKey(
        "location.Country", related_name="cities", on_delete=models.CASCADE
    )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ NAME
    # └─────────────────────────────────────────────────────────────────────────────────

    name = models.CharField(max_length=255)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ POPULATION
    # └─────────────────────────────────────────────────────────────────────────────────

    population = models.IntegerField()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COORDINATES
    # └─────────────────────────────────────────────────────────────────────────────────

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self):
        """ Custom String Method """

        # Return name
        return self.name

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:

        # Define verbose names
        verbose_name = "City"
        verbose_name_plural = "Cities"

        # Define unique together constraints
        unique_together = [["latitude", "longitude"]]


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY
# └─────────────────────────────────────────────────────────────────────────────────────


class Country(models.Model):
    """ Country Model """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CAPITAL
    # └─────────────────────────────────────────────────────────────────────────────────

    capital = models.OneToOneField(
        "location.City",
        related_name="capital_country",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ NAME
    # └─────────────────────────────────────────────────────────────────────────────────

    name = models.CharField(max_length=255, unique=True)
    name_native = models.CharField(max_length=255, unique=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ISO
    # └─────────────────────────────────────────────────────────────────────────────────

    iso2 = models.CharField(max_length=2, unique=True)
    iso3 = models.CharField(max_length=3, unique=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ POPULATION
    # └─────────────────────────────────────────────────────────────────────────────────

    population = models.IntegerField(blank=True, null=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COORDINATES
    # └─────────────────────────────────────────────────────────────────────────────────

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UN MEMBER STATUS
    # └─────────────────────────────────────────────────────────────────────────────────

    is_un_member = models.BooleanField()
    is_un_member_at = models.DateTimeField(blank=True, null=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FLAG
    # └─────────────────────────────────────────────────────────────────────────────────

    FLAG_UPLOAD_TO = "location/country/flag"  # Makes this accessible in migration

    flag = models.ImageField(upload_to=FLAG_UPLOAD_TO)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self):
        """ Custom String Method """

        # Return name
        return self.name

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLEAN
    # └─────────────────────────────────────────────────────────────────────────────────

    def clean(self):
        """ Custom Clean Method """

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ ISO
        # └─────────────────────────────────────────────────────────────────────────────

        # Uppercase and strip ISO codes
        self.iso2, self.iso3 = [iso.upper().strip() for iso in (self.iso2, self.iso3)]

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ UN MEMBER STATUS
        # └─────────────────────────────────────────────────────────────────────────────

        # Check if is UN member
        if self.is_un_member:

            # Check if is UN member at is null
            if not self.is_un_member_at:

                # Raise ValidationError
                raise ValidationError(
                    "Country.is_un_member_at cannot be null if Country.is_un_member "
                    "is True"
                )

        # Otherwise handle non-UN member
        else:

            # Nullify is UN member at
            self.is_un_member_at = None

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SAVE
    # └─────────────────────────────────────────────────────────────────────────────────

    def save(self, *args, **kwargs):
        """ Custom Save Method """

        # Clean object
        self.clean()

        # Save object
        return super().save(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:

        # Define verbose names
        verbose_name = "Country"
        verbose_name_plural = "Countries"

        # Define unique together constraints
        unique_together = [["latitude", "longitude"]]
