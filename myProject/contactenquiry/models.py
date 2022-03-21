from django.db import models
from autoslug import AutoSlugField

class saveEnquiry(models.Model):
	my_name = models.CharField(max_length=50);
	my_email = models.CharField(max_length=50);
	my_mno = models.CharField(max_length=15);
	my_websitename = models.CharField(max_length=50);
	my_message = models.CharField(max_length=250);
	# we also make internal slug's on the bases of my_name, may be in future we needed these! 
	slug = AutoSlugField(populate_from='my_name', unique=True, null=True, default=None);

	# we adding this field because we want to add image's too.
	my_image = models.FileField(upload_to="news/",max_length=250,null=True,default=None);

	"""
	# this is also one of the best consept, but we implementing this in the future...
	def __str__(self):
		return self.my_name+" is Inserted details.";
	"""


 

# Create your models here.


