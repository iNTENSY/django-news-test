from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        slug_field='name', read_only=True
    )

    class Meta:
        model = News
        fields = ('tag', 'title', 'text', 'visit_count', 'pk')
