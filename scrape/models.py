from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
class Detail(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name