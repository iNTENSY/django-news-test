from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Tag(models.Model):
    """
    Данная модель используется в качестве
    тегов для новостей.
    """
    name = models.CharField(
        verbose_name='Наименование',
        max_length=20
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    """
    Модель новостей, которая включает в себя
    наименование, текст, картинку и лайки каждого
    отдельного объекта.
    """
    tag = models.ManyToManyField(
        to=Tag,
        verbose_name='Тег',
        blank=True,
        related_name='news'
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        null=True,
        blank=True,
        default=None,
        upload_to='news/images'
    )
    like = models.ManyToManyField(
        to=User,
        verbose_name='Лайки',
        blank=True,
        related_name='news_likes'
    )
    dislike = models.ManyToManyField(
        to=User,
        verbose_name='Дизлайк',
        blank=True,
        related_name='news_dislikes'
    )
    visit_count = models.PositiveIntegerField(
        verbose_name='Кол-во посещений',
        default=0
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-id',)

    def __str__(self):
        return self.title[:50] + '...' if len(self.title) > 50 else self.title

    def get_absolute_url(self) -> str:
        return reverse('news:detail', kwargs={'pk': self.pk})
