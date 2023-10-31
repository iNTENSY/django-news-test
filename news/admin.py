from django.contrib import admin

from news.models import News, Tag

# Register your models here.
admin.site.register(News)
admin.site.register(Tag)