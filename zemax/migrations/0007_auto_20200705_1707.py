# Generated by Django 3.0.8 on 2020-07-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0006_auto_20200705_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, default='default.png', upload_to='house_pics'),
        ),
    ]