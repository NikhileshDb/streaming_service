# Generated by Django 3.2.9 on 2021-11-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storefile',
            name='mediaFile',
            field=models.FileField(upload_to='media/'),
        ),
    ]