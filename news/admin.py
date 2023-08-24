from django.contrib import admin
from news.models import Categories, News, Users

# Register your models here.
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(News)
