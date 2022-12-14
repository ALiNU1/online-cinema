from django.db import models

# Create your models here.

class Category(models.Model):
    """Категории"""
    title = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

