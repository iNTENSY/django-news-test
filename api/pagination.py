from rest_framework import pagination


class NewsListPagination(pagination.LimitOffsetPagination):
    default_limit = 3