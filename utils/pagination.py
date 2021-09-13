# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from dynamic_rest.pagination import DynamicPageNumberPagination


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DYNAMIC PAGINATION
# └─────────────────────────────────────────────────────────────────────────────────────


class DynamicPagination(DynamicPageNumberPagination):
    """ A dynamic pagination class for querysets """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define page size and max page size
    page_size = 20
    max_page_size = 100

    # Define page query params
    page_query_param = "page"
    page_size_query_param = "page_size"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET PAGE METADATA
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_page_metadata(self):
        """ Constructs the metadata for the paginated response """

        # Return page metadata
        return {
            self.page_query_param: self.page.number,
            self.page_size_query_param: self.get_page_size(self.request),
            "page_count": self.page.paginator.num_pages,
            "result_count": self.page.paginator.count,
        }
