from django.contrib import admin

from .models import *

class NeighborhoodAdmin(admin.ModelAdmin):
    filter_horizontal =('user_profile')

admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(User_profile)
