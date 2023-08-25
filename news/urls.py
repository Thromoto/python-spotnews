from django.urls import path
from news.views import index, news_details, categories_form, news_form


urlpatterns = [
    path("news/<int:id>", news_details, name="news-details-page"),
    path("news/", news_form, name="news-form"),
    path("categories/", categories_form, name="categories-form"),
    path("", index, name="home-page"),
]
