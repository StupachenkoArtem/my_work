# Generated by Django 4.2.7 on 2023-12-13 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mikhalchuk', '0007_collection_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jackets',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newcollection',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shirtsandblouses',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trousersandskirts',
            name='user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
