# Generated by Django 4.1.4 on 2023-11-27 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_is_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_doc',
            new_name='is_doctor',
        ),
    ]