# Generated by Django 5.1.1 on 2024-09-12 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_cantact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cantact',
            new_name='Contact',
        ),
    ]