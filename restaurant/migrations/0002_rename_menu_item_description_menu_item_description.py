# Generated by Django 4.2.3 on 2023-07-17 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_item_description',
            new_name='item_description',
        ),
    ]
