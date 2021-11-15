# Generated by Django 3.2.9 on 2021-11-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211114_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encodedfiles',
            old_name='dash_output',
            new_name='dash_output_url',
        ),
        migrations.RenameField(
            model_name='encodedfiles',
            old_name='hls_output',
            new_name='hls_output_url',
        ),
        migrations.AddField(
            model_name='dataencoder',
            name='dash_output',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='dataencoder',
            name='hls_output',
            field=models.URLField(blank=True),
        ),
    ]