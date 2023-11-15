from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    # This line is used to make the search keyword customize as needed in the browsable api.
    cursor_query_param = 'cu'
    