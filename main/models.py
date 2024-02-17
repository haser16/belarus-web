from django.db import models


class Medicine(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='medicine')

    def __str__(self):
        return f'{self.description}'


class Industry(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='medicine')

    def __str__(self):
        return f'{self.description}'


class Construction(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='construction')

    def __str__(self):
        return f'{self.description}'


class CarBuilding(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='carbuilding')

    def __str__(self):
        return f'{self.description}'


class Agriculture(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='agriculture')

    def __str__(self):
        return f'{self.description}'


class Forestry(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='forestry')

    def __str__(self):
        return f'{self.description}'


class IT(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='it')

    def __str__(self):
        return f'{self.description}'


class Culture(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='culture')

    def __str__(self):
        return f'{self.description}'


class Architecture(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='architecture')

    def __str__(self):
        return f'{self.description}'


class Images(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.name}'
