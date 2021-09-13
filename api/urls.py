# ┌────────────────────────────────────────────────────────────────────────────────────┐
# │ DJANGO IMPORTS                                                                     │
# └────────────────────────────────────────────────────────────────────────────────────┘

from django.urls import path

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.routers import DynamicRouter
from rest_framework_nested.routers import NestedDefaultRouter

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from location.views import CityViewSet, CountryViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ API ROUTER
# └─────────────────────────────────────────────────────────────────────────────────────

# api_root (/)
router = DynamicRouter()

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOCATION
# └─────────────────────────────────────────────────────────────────────────────────────

# cities/
router.register("cities", CityViewSet, base_name="cities")

# countries/
router.register("countries", CountryViewSet, base_name="countries")

# Define countries router
countries_router = NestedDefaultRouter(router, "countries", lookup="country")

# countries/:id/cities/(:id)
# countries_router.register(
#    "cities",
#    TransactionOfAccountReadOnlyViewSet,
#    basename="transactions-of-account",
# )

# ┌────────────────────────────────────────────────────────────────────────────────────┐
# │ URL PATTERNS                                                                       │
# └────────────────────────────────────────────────────────────────────────────────────┘

# Initialize URL patterns list
urlpatterns = []

# Define router URLs
router_urls = [
    # Router urls
    router.urls,
    # Nested router urls
    countries_router.urls,
]

# Concatenate all lists
for router_url in router_urls:
    urlpatterns += router_url
