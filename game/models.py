from django.db import models


class Icons(models.Model):
    image = models.FileField(upload_to='icons')
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'
