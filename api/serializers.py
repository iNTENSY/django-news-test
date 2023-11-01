from rest_framework import serializers

from news.models import News, Tag


class NewsSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = News
        fields = ('tag', 'title', 'text', 'visit_count', 'pk')
        read_only_fields = ('visit_count', 'pk')
