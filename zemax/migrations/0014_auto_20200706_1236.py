# Generated by Django 3.0.8 on 2020-07-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zemax', '0013_auto_20200706_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(default='default.png', upload_to='house_pics'),
        ),
    ]