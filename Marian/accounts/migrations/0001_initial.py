# Generated by Django 4.1.3 on 2022-11-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=50, null=True, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=50, null=True, verbose_name='Full name')),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Phone Number')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/Accounts', verbose_name='Account image')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff user')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active user')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
