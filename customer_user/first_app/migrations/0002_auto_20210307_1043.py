# Generated by Django 3.1.2 on 2021-03-07 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_koined',
            new_name='date_joined',
        ),
    ]
