# Generated by Django 3.0.8 on 2020-07-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0007_auto_20200705_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]