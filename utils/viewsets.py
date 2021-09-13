# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import filters


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DYNAMIC MODEL VIEWSET
# └─────────────────────────────────────────────────────────────────────────────────────


class DynamicModelViewSet(DynamicModelViewSet):
    """ An extension of Dynamic REST's DynamicModelViewSet """

    # Apply DRF search filter backend
    filter_backends = DynamicModelViewSet.filter_backends + (filters.SearchFilter,)


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DYNAMIC READ ONLY MODEL VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class DynamicReadOnlyModelViewSet(DynamicModelViewSet):
    """ A read-only implementation of DynamicModelViewSet """

    # Restrict HTTP methods to safe methods
    http_method_names = ["get", "head", "options"]
