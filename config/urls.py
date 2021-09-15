# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ URL PATTERNS
# └─────────────────────────────────────────────────────────────────────────────────────

# URL Patterns List
urlpatterns = [path("api/", include("api.urls"))]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────

# Admin URL Pattern
if settings.ENABLE_DJANGO_ADMIN:

    # Get environment reminder
    environment_reminder = settings.ENVIRONMENT.title()

    # Define title from environment reminder
    TITLE = f"DRF Demo {environment_reminder}"

    # Set title for Django Admin
    admin.site.site_title = TITLE
    admin.site.site_header = TITLE
    admin.site.index_title = "Admin Panel"

    # Add Django Admin URL patterns
    urlpatterns += [path("admin/", admin.site.urls)]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ BROWSABLE API
# └─────────────────────────────────────────────────────────────────────────────────────

# Browsable API URL Pattern
if settings.ENABLE_BROWSABLE_API:

    # Add browsable API URL patterns
    urlpatterns += [path("auth/", include("rest_framework.urls"))]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOCAL STORAGE
# └─────────────────────────────────────────────────────────────────────────────────────

# Check if local storage is enabled
if settings.ENVIRONMENT == settings.LOCAL and settings.USE_LOCAL_STORAGE:

    # Add local static and media URLs
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
