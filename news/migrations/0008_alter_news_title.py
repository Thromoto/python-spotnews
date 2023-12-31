# Generated by Django 4.2.3 on 2023-08-22 21:09

from django.db import migrations, models
import news.models.news_model


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0007_alter_news_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[news.models.news_model.validate_title],
            ),
        ),
    ]
