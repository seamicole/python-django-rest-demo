# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.routers import DynamicRouter
from rest_framework_nested.routers import NestedDefaultRouter

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from currency.views import CurrencyViewSet
from location.views import (
    CityOfCountryViewSet,
    CityViewSet,
    CountryOfCurrencyViewSet,
    CountryViewSet,
)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ API ROUTER
# └─────────────────────────────────────────────────────────────────────────────────────

# api_root (/)
router = DynamicRouter()

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CURRENCY
# └─────────────────────────────────────────────────────────────────────────────────────

# currencies/
router.register("currencies", CurrencyViewSet, base_name="currencies")

# Define currencies router
currencies_router = NestedDefaultRouter(router, "currencies", lookup="currency")

# currencies/:id/countries/(:id)
currencies_router.register(
    "countries", CountryOfCurrencyViewSet, basename="countries-of-currency"
)

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
countries_router.register("cities", CityOfCountryViewSet, basename="cities-of-country")

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
    currencies_router.urls,
]

# Concatenate all lists
for router_url in router_urls:
    urlpatterns += router_url
