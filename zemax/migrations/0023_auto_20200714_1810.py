# Generated by Django 3.0.8 on 2020-07-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0022_auto_20200713_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_image',
            field=models.ImageField(blank=True, upload_to='house_pics'),
        ),
    ]