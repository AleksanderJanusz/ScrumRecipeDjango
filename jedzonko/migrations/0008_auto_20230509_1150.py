# Generated by Django 2.2.6 on 2023-05-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0007_merge_20230509_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]