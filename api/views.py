from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializers import NewsSerializer
from news.models import News


class NewsViewSet(viewsets.ModelViewSet):
    """
    Стандартынй вьюсет для модели News включая пагинацию,
    фильтр по тегу, фильтр по поиску названия.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('tag__name',)
    search_fields = ('title',)

    @action(methods=['get', 'post'], url_path='news-action', detail=True)
    def news_action(self, *args, **kwargs):
        """
        Данный метод позволяет использовать путь .../news/<pk>/news-action
        только по get- или post-запросу. Данный метод обрабатывает нажатие
        лайка и дизлайка на странице новости.
        По get-запросу возвращается список лайков и дизлайков.
        По post-запросу возвращается сериализованный объект модели новости.
        """

        if self.request.method == 'GET':
            return Response(self.get_likes())
        return Response(self.like_dislike_updater())

    def get_likes(self):
        news = self.get_object()
        likes_count = news.like.all().count()
        dislikes_count = news.dislike.all().count()
        return {'like_count': likes_count,
                'dislike_count': dislikes_count}

    def like_dislike_updater(self):
        action = self.request.POST.get('action')
        news = self.get_object()

        match action:
            case 'like':
                self.like(news)
            case 'dislike':
                self.dislike(news)
        news.save()
        serializer = self.get_serializer(news)
        return serializer.data

    def like(self, news):
        if self.request.user not in news.like.all():
            news.like.add(self.request.user)
        else:
            news.like.remove(self.request.user)
        return news

    def dislike(self, news):
        if self.request.user not in news.dislike.all():
            news.dislike.add(self.request.user)
        else:
            news.dislike.remove(self.request.user)
        return news
