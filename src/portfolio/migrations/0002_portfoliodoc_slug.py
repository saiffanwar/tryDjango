# Generated by Django 4.2 on 2023-04-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliodoc',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=120),
            preserve_default=False,
        ),
    ]