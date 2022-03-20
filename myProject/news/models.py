from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
	news_title = models.CharField(max_length=100);
	news_desc = HTMLField(); 
	slug = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None);


# Create your models here.
"""
	# Related to lecture-45, slug related passing parameters details...
    slug = AutoSlugField(populate_from=lambda instance: instance.title,
                         unique_with=['author__name', 'pub_date__month'],
                         slugify=lambda value: value.replace(' ','-'))
"""