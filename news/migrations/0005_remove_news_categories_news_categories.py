# Generated by Django 4.2.3 on 2023-08-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_rename_create_at_news_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="categories",
        ),
        migrations.AddField(
            model_name="news",
            name="categories",
            field=models.ManyToManyField(to="news.categories"),
        ),
    ]