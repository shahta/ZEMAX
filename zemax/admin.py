from django.contrib import admin
from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('address', 'id', 'price', 'square_feet', 'year', 'agent', 'contact')


admin.site.register(House, HouseAdmin)

