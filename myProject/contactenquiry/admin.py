from django.contrib import admin
from contactenquiry.models import saveEnquiry

class saveEnquiryAdmin(admin.ModelAdmin):
	list_display=('my_name', 'my_email', 'my_mno', 'my_websitename', 'my_message');
admin.site.register(saveEnquiry,saveEnquiryAdmin);





# Register your models here.

"""
class saveEnquiry(models.Model):
	my_name = models.CharField(max_length=50);
	my_email = models.CharField(max_length=50);
	my_mno = models.CharField(max_length=15);
	my_websitename = models.CharField(max_length=50);
	my_message = models.CharField(max_length=250);
	# we also make internal slug's on the bases of my_name, may be in future we needed these! 
	slug = AutoSlugField(populate_from='my_name', unique=True, null=True, default=None);
"""



