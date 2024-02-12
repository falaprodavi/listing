# Generated by Django 5.0.1 on 2024-02-12 11:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', ckeditor.fields.RichTextField()),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]