# Generated by Django 4.2.4 on 2023-09-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название платья')),
                ('compound', models.CharField(max_length=255, verbose_name='состав')),
                ('color', models.CharField(max_length=255, verbose_name='цвет')),
                ('photo', models.ImageField(upload_to='')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]