from django.contrib import admin

from news.models import News, Tag

admin.site.register(Tag)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag', 'like', 'dislike')
    list_display = ('title', 'get_count_like', 'get_count_dislike')
    readonly_fields = ('get_count_like', 'get_count_dislike')

    def get_count_like(self, obj):
        return len(obj.like.all())

    def get_count_dislike(self, obj):
        return len(obj.dislike.all())

    get_count_like.short_description = 'Количество лайков'
    get_count_dislike.short_description = 'Количество дизлайков'