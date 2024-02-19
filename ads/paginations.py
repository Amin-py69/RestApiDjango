from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50
    # page_size = getattr(settings, 'PAGINATION_PAGE_SIZE', 1)
