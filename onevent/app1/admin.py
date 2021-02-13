from django.contrib import admin

# Register your models here.

from app1.models import Events

class eventsAdmin(admin.ModelAdmin):
        list_display=["eventname",'banner','eventname','eventdescription', 'event_type']
admin.site.register(Events,eventsAdmin)
