from django.db import models

# Create your models here.
<<<<<<< HEAD
class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
=======
>>>>>>> fbad417bf1a3a52ae6033210a347b54d46757b2a
