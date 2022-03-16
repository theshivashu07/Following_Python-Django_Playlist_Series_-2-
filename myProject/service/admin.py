from django.contrib import admin
from service.models import Service,trialData
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
	list_display=('service_icon','service_title', 'service_des')
admin.site.register(Service,ServiceAdmin)

"""
# We also pass this, but then one last field is hidden,
# And whenever we want it back, so we again adding this.
class ServiceAdmin(admin.ModelAdmin):
	list_display=('service_icon','service_title')
admin.site.register(Service,ServiceAdmin)
"""

class trialDataAdmin(admin.ModelAdmin):
	list_display=('head_data','class_name')
admin.site.register(trialData,trialDataAdmin)




