# Generated by Django 3.2 on 2021-05-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210522_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='phone',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='desc',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
    ]
