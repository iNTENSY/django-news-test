# Generated by Django 4.2.6 on 2023-10-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]