# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ADMIN
# └─────────────────────────────────────────────────────────────────────────────────────

# Get environment reminder
environment_reminder = settings.ENVIRONMENT.title()

# Define title from environment reminder
TITLE = f"DRF Showcase {environment_reminder}"

# Set title for Django Admin
admin.site.site_title = TITLE
admin.site.site_header = TITLE
admin.site.index_title = "Admin Panel"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ URL PATTERNS
# └─────────────────────────────────────────────────────────────────────────────────────

# URL Patterns List
urlpatterns = [path("admin/", admin.site.urls), path("api/", include("api.urls"))]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ BROWSABLE API
# └─────────────────────────────────────────────────────────────────────────────────────

# Browsable API URL Pattern
if settings.ENABLE_BROWSABLE_API:

    # Browsable API
    urlpatterns += [path("auth/", include("rest_framework.urls"))]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOCAL STORAGE
# └─────────────────────────────────────────────────────────────────────────────────────

# Check if local storage is enabled
if settings.ENVIRONMENT == settings.LOCAL and settings.USE_LOCAL_STORAGE:

    # Add local static and media URLs
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
