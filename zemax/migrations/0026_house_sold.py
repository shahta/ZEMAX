# Generated by Django 3.0.8 on 2020-07-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0025_auto_20200714_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
