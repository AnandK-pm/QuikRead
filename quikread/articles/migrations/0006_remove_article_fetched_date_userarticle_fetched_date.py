# Generated by Django 5.1.2 on 2024-10-26 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_fetched_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='fetched_date',
        ),
        migrations.AddField(
            model_name='userarticle',
            name='fetched_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
