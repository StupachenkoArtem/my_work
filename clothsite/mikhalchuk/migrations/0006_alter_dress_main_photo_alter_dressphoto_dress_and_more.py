# Generated by Django 4.2.7 on 2023-12-03 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mikhalchuk', '0005_dress_jackets_newcollection_shirtsandblouses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='main_photo',
            field=models.ImageField(upload_to='Dress_photos'),
        ),
        migrations.AlterField(
            model_name='dressphoto',
            name='Dress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikhalchuk.dress'),
        ),
        migrations.AlterField(
            model_name='dressphoto',
            name='image',
            field=models.ImageField(upload_to='Dress_photos'),
        ),
        migrations.AlterField(
            model_name='jackets',
            name='main_photo',
            field=models.ImageField(upload_to='Jackets_photos'),
        ),
        migrations.AlterField(
            model_name='jacketsphoto',
            name='Jackets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikhalchuk.jackets'),
        ),
        migrations.AlterField(
            model_name='jacketsphoto',
            name='image',
            field=models.ImageField(upload_to='Jackets_photos'),
        ),
        migrations.AlterField(
            model_name='newcollection',
            name='main_photo',
            field=models.ImageField(upload_to='NewCollection_photos'),
        ),
        migrations.AlterField(
            model_name='newcollectionphoto',
            name='NewCollection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikhalchuk.newcollection'),
        ),
        migrations.AlterField(
            model_name='newcollectionphoto',
            name='image',
            field=models.ImageField(upload_to='NewCollection_photos'),
        ),
        migrations.AlterField(
            model_name='shirtsandblouses',
            name='main_photo',
            field=models.ImageField(upload_to='ShirtsAndBlouses_photos'),
        ),
        migrations.AlterField(
            model_name='shirtsandblousesphoto',
            name='ShirtsAndBlouses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikhalchuk.shirtsandblouses'),
        ),
        migrations.AlterField(
            model_name='shirtsandblousesphoto',
            name='image',
            field=models.ImageField(upload_to='ShirtsAndBlouses_photos'),
        ),
        migrations.AlterField(
            model_name='trousersandskirts',
            name='main_photo',
            field=models.ImageField(upload_to='TrousersAndSkirts_photos'),
        ),
        migrations.AlterField(
            model_name='trousersandskirtsphoto',
            name='TrousersAndSkirts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mikhalchuk.trousersandskirts'),
        ),
        migrations.AlterField(
            model_name='trousersandskirtsphoto',
            name='image',
            field=models.ImageField(upload_to='TrousersAndSkirts_photos'),
        ),
    ]
