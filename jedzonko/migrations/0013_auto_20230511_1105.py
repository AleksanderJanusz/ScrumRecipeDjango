# Generated by Django 2.2.6 on 2023-05-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0012_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(auto_created='djangodbmodelsfieldscharfield', unique=True),
        ),
    ]