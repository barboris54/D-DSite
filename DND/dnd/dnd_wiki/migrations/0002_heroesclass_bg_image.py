# Generated by Django 4.1.4 on 2023-05-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroesclass',
            name='bg_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
