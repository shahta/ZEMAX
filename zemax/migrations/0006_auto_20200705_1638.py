# Generated by Django 3.0.8 on 2020-07-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0005_house_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
