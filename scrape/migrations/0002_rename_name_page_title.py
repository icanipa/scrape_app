# Generated by Django 4.2.6 on 2023-10-23 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='name',
            new_name='title',
        ),
    ]
