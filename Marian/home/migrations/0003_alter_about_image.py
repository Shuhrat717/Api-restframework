# Generated by Django 4.1.3 on 2022-11-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='static/About'),
        ),
    ]
