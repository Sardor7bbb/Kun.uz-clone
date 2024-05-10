from django.db import models

# Create your models here.


class News(models.Model):
    objects = None
    title = models.CharField(max_length=200, verbose_name='Title')
    info = models.TextField()
    set_data = models.DateTimeField(auto_now_add=True, verbose_name='Set Data')
    link = models.URLField(verbose_name='Link')
    image = models.ImageField(verbose_name='Image', upload_to='news/')

    def __str__(self):
        return self.title

