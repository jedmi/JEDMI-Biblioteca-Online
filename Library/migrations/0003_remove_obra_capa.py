# Generated by Django 2.0.6 on 2018-06-11 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_obra_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='capa',
        ),
    ]