from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
# from .models import Drywaste, Tracksheet,Lanedetails,LaneCordinator
from .models import Tracksheet,DutyEntry,Feedback

admin.site.register(Tracksheet)
admin.site.register(DutyEntry)
admin.site.register(Feedback)
class Feedback(OSMGeoAdmin):
    list_display = ('name', 'location')