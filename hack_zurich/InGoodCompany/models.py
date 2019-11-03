from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    score = models.FloatField(max_length=10, default=None)
    words_frequency_image = models.ImageField(upload_to='images/', default='pic_folder/None/no-img.jpg')

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
