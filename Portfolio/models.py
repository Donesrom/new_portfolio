from django.db import models

from tinymce import models as tinymce_models

# Create your models here.

class About(models.Model):
    Title= models.CharField(max_length= 70)
    Description = models.TextField()

    def __str__(self):
        return self.Title

class Services(models.Model):
    Title= models.CharField(max_length= 70)
    Description = models.TextField()
    icon= models.ImageField(upload_to= 'pics', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.Title


class Projects(models.Model):
    Title= models.CharField(max_length=70)
    Description= tinymce_models.HTMLField(null=True, default= 'Yes')
    Project_link = tinymce_models.HTMLField( default= 'Yes')

    def __str__(self):
        return self.Title