from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Routes)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Bus)
admin.site.register(CurrentLocation)
admin.site.register(LocationHistory)
