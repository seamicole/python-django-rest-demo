# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.contrib import admin

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from user.models import User


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────


class UserAdmin(admin.ModelAdmin):
    """ User Admin """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define list display
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "is_active",
        "is_staff",
        "is_superuser",
    ]

    # Define list display links
    list_display_links = ["id", "email"]

    # Define search fields
    search_fields = ["first_name", "last_name", "email"]


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ REGISTER
# └─────────────────────────────────────────────────────────────────────────────────────

admin.site.register(User, UserAdmin)
