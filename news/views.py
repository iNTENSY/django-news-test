from django.views import generic

from news.filters import NewsFilter
from news.models import News


class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object()
        post.visit_count += 1
        post.save()
        return post


class IndexView(generic.TemplateView):
    template_name = 'news/list.html'


class StatisticListView(generic.ListView):
    model = News
    template_name = 'news/statistic.html'
    context_object_name = 'news'
    paginate_by = 10


class MyFilterView(generic.ListView):
    """ Отображение страницы с фильтром """

    model: object = News
    template_name: str = 'news/filters_by_tag.html'
    context_object_name: str = 'rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        context: dict = super(MyFilterView, self).get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
                                       queryset=self.get_queryset())
        return context
