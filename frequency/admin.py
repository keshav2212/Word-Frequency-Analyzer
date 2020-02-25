from django.contrib import admin
from .models import givenurl,resulttable
from django.contrib.admin.models import LogEntry
class resultadmin(admin.ModelAdmin):
	list_display=['URL','Keyword','wordfrequency']
	list_editable=['Keyword','wordfrequency']
admin.site.register(givenurl)
admin.site.register(resulttable,resultadmin)
admin.site.register(LogEntry)
# Register your models here.
