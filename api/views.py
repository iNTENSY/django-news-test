from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework import filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import NewsSerializer
from news.models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('tag__name',)
    search_fields = ('title',)


class UpdateLikesDislikes(APIView):
    def post(self, *args, **kwargs):
        action = self.request.POST.get('action')[0]
        print(self.request.POST)
        return JsonResponse({'status': 'okkk'})