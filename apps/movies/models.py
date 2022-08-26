from datetime import date
from django.db import models
from apps.categories.models import Category
from django.core.validators import FileExtensionValidator
# Create your models here.


# Create your models here.
class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Actor(models.Model):
    name= models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"

class Directors(models.Model):
    """Режиссеры"""
    name= models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to="directors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Режиссер"
        verbose_name_plural= "Режиссеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    duration = models.IntegerField("Длительность", default=0)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    GENRE_CHOICES = (
        ('Боевики', 'Боевики'),
        ('Комедии', 'Комедии'),
        ('Фантастика/фэнтези', 'Фантастика/фэнтези'),
        ('Мультфильмы', 'Мультфильмы'),
        ('Драма/мелодрама', 'Драма/мелодрама'),
        ('Ужасы', 'Ужасы'),
        ('Детектив/Триллеры', 'Детектив/Триллеры'),
        ('Документальные', 'Документальные'),
    )
    country = models.CharField("Страна", max_length=30)
    directors = models.ForeignKey(Directors, verbose_name="режиссер", related_name="film_director", on_delete= models.CASCADE)
    actors = models.ForeignKey(Actor, verbose_name="актеры", related_name="film_actor", on_delete= models.CASCADE)
    genres = models.ForeignKey(Genre, verbose_name="жанры", on_delete= models.CASCADE)
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    fees_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(Category, verbose_name="Категория",blank=True, null=True, on_delete= models.CASCADE)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    premiere= models.BooleanField("Премьера", default=False)

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'image/', blank = True, null = True)
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"