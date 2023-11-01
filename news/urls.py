from django.urls import path, re_path

from news import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^news/(?P<pk>\d+)/$', views.NewsDetail.as_view(), name='detail'),
    path('statistic/', views.StatisticListView.as_view(), name='statistic'),
    path('filter/', views.MyFilterView.as_view(), name='filter')
]
