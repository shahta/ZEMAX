from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class House(models.Model):
    house_image = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True, max_length=1500,
                                    verbose_name='House Image')
    house_image2 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image3 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image4 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image5 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image6 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image7 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image8 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image9 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image10 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image11 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image12 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image13 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image14 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image15 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image16 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    house_image17 = models.ImageField(default='default.jpg', upload_to='house_pics', blank=True)
    address = models.CharField(max_length=255)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    square_feet = models.IntegerField()
    description = models.TextField()
    year = models.IntegerField(default=2020)
    agent = models.CharField(max_length=255)
    contact = models.EmailField(max_length=255)
    sold = models.BooleanField(default=False, verbose_name='Already Sold?')

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})





