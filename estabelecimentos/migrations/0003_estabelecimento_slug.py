# Generated by Django 5.0.1 on 2024-01-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0002_rename_imovel_estabelecimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
