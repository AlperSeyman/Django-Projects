# Generated by Django 5.1.1 on 2025-03-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='describtion',
            new_name='description',
        ),
    ]
