# Generated by Django 3.0.8 on 2020-07-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0026_house_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='sold',
            field=models.BooleanField(default=False, verbose_name='Already Sold?'),
        ),
    ]