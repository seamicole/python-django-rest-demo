# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.viewsets import DynamicModelViewSet


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DYNAMIC READ ONLY MODEL VIEW SET
# └─────────────────────────────────────────────────────────────────────────────────────


class DynamicReadOnlyModelViewSet(DynamicModelViewSet):
    """ A read-only implementation of DynamicModelViewSet """

    # Restrict HTTP methods to safe methods
    http_method_names = ["get", "head", "options"]
