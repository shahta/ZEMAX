# Generated by Django 3.0.8 on 2020-07-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0016_house_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image3',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='house_pics'),
        ),
    ]
