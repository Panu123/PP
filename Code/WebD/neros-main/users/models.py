
from distutils.command.upload import upload

from django.contrib.auth.models import User 

from django.db import models
from django.db import models

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit import processors
from imagekit.processors import ResizeToFill


#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.db import models




class Picture(models.Model):
    
    name = models.CharField(max_length=50,primary_key=True, unique=True)
    picture_Main_Img = models.ImageField(upload_to='images/')
    
    picture_thumbnail = ImageSpecField(source='picture_Main_Img', processors=[ResizeToFill(300, 200)], format='JPEG', options={'quality':60})
    # picture_thumbnail2 = ImageSpecField(source='picture_Main_Img',  processors=[ResizeToFill (200, 100)],format='JPEG', options={'quality':60})
    
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
    
    def __str__(self):
        return self.name



    def delete(self, *args, **kwargs):
        self.picture_Main_Img.delete() 
        super().delete(*args, **kwargs)

picture = Picture.objects.all()[0]
print(picture.picture_thumbnail.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
print(picture.picture_thumbnail.width)  # > 100