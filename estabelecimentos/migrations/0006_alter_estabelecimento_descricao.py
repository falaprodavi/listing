# Generated by Django 5.0.1 on 2024-01-30 14:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0005_estabelecimento_destaque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='descricao',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
