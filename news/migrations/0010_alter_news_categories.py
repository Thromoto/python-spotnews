# Generated by Django 4.2.3 on 2023-08-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0009_alter_news_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="categories",
            field=models.ManyToManyField(to="news.categories"),
        ),
    ]