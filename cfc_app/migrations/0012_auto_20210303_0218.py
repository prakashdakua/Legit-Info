# Generated by Django 3.0.8 on 2021-03-03 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0011_auto_20210303_0157'),
    ]

    operations = [
    migrations.RenameField('Hash', 'desc', 'legdesc'),
    migrations.RenameField('Hash', 'size', 'objsize'),
    ]
