from django.views import generic

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

