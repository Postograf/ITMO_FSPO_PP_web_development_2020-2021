# Generated by Django 3.1.7 on 2021-03-27 13:15

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0007_auto_20210327_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='passport_number',
            field=models.DecimalField(decimal_places=0, max_digits=6, unique=True),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]