# Generated by Django 4.1.5 on 2023-01-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_produto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='artista',
            field=models.CharField(default='', max_length=200, verbose_name='Artista'),
        ),
    ]
