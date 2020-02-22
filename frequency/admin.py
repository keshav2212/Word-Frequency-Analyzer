from django.contrib import admin
from .models import givenurl,resulttable
class resultadmin(admin.ModelAdmin):
	list_display=['Keyword','wordfrequency','URL']
admin.site.register(givenurl)
admin.site.register(resulttable,resultadmin)
# Register your models here.
