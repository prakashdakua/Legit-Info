# Generated by Django 3.0.8 on 2020-07-31 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
