# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.contrib import admin

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from location.models import City, Country


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CITY ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────


class CityAdmin(admin.ModelAdmin):
    """ City Admin """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define list display
    list_display = ["id", "name", "country", "population", "latitude", "longitude"]

    # Define list display links
    list_display_links = ["id", "name"]

    # Define search fields
    search_fields = ["name"]


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────


class CountryAdmin(admin.ModelAdmin):
    """ Country Admin """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define list display
    list_display = [
        "id",
        "name",
        "name_native",
        "iso2",
        "iso3",
        "population",
        "latitude",
        "longitude",
        "is_un_member",
    ]

    # Define list display links
    list_display_links = ["id", "name"]

    # Define search fields
    search_fields = ["name", "name_native"]


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ REGISTER
# └─────────────────────────────────────────────────────────────────────────────────────

admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
