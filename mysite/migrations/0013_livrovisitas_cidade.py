# Generated by Django 4.1.5 on 2023-01-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_remove_livrovisitas_recomenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='livrovisitas',
            name='cidade',
            field=models.CharField(default='', max_length=30, verbose_name='Cidade'),
        ),
    ]