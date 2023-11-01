from django.urls import path, include
from rest_framework import routers

from api.views import NewsViewSet


app_name = 'api'


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('v1/', include(router.urls)),
]
