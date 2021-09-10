from django.db import models

      
class Image(models.Model):
    name                   = models.CharField(max_length=1000, null=True, blank=True)
    image               = models.FileField(upload_to='img/', null=True, blank=True)
    
    def __str__(self):
        return str(self.image)
   