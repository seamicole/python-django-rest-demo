# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db import models


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY
# └─────────────────────────────────────────────────────────────────────────────────────


class Currency(models.Model):
    """ Currency Model """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COUNTRY
    # └─────────────────────────────────────────────────────────────────────────────────

    country = models.ForeignKey(
        "location.Country",
        related_name="currencies",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ NAME
    # └─────────────────────────────────────────────────────────────────────────────────

    name = models.CharField(max_length=255)
    name_plural = models.CharField(max_length=255)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CODE / NUMBER
    # └─────────────────────────────────────────────────────────────────────────────────

    code = models.CharField(max_length=10, unique=True)
    number = models.PositiveIntegerField(unique=True, blank=True, null=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SYMBOLS
    # └─────────────────────────────────────────────────────────────────────────────────

    symbol = models.CharField(max_length=10)
    symbol_native = models.CharField(max_length=20)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FLAG
    # └─────────────────────────────────────────────────────────────────────────────────

    flag = models.ImageField(upload_to="currency/currency/flag")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __STR__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __str__(self):
        """ Custom String Method """

        # Return name
        return self.name

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FLAG OR COUNTRY FLAG
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def flag_or_country_flag(self):
        """ Returns the currency or country flag depending on which exists """

        # Return currency flag or country flag
        return self.flag or (self.country_id and self.country.flag)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:

        # Define verbose names
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
