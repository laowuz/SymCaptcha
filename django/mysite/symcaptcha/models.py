from django.db import models

# Create your models here.

class ImgSymLabel(models.Model):
    imgname = models.CharField(blank=False,max_length=64)
    category = models.CharField(max_length=32)
    labeltime = models.DateTimeField(blank=False)
    sympoints = models.CharField(max_length=64)
    labelusr = models.CharField(max_length=32)

    def __unicode__(self):
        return self.imgname

