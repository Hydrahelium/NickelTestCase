from django.contrib import admin
from .models import Stock, Timefeed
# Register your models here.

admin.site.register(Stock)
admin.site.register(Timefeed)
