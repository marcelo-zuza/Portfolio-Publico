# Generated by Django 4.1.5 on 2023-01-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_produto_descricao_alter_produto_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug'),
        ),
    ]