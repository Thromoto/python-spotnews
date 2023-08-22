from django.db import models
from django.core.exceptions import ValidationError
from news.models.category_model import Categories
from news.models.user_model import Users


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_title],
        blank=False,
        )
    content = models.TextField(
        max_length=None,
        blank=False,
        help_text={'<content>': ['Este campo não pode estar vazio.']}
        )
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
