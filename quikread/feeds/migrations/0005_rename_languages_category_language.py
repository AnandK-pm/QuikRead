# Generated by Django 5.1.2 on 2024-11-09 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_category_languages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='languages',
            new_name='language',
        ),
    ]