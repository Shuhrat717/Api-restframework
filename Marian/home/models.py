from django.db import models


class About(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField()
    image = models.ImageField(upload_to='static/About')

    def __str__(self):
        return self.title


class Service(models.Model):
    service_icon = models.ImageField(upload_to='static/Service_icon')
    service_title = models.CharField(max_length=212)
    service_content = models.TextField()
    image = models.ImageField(upload_to='static/Service')

    def __str__(self):
        return self.service_title
