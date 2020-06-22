# Generated by Django 3.0.3 on 2020-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_categoty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categoty',
            field=models.CharField(choices=[('SPORT', 'sport'), ('POLITICS', 'politics'), ('FILMS', 'films'), ('NEWS', 'news')], default='news', max_length=100),
        ),
    ]
