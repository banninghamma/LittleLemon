# Generated by Django 4.2.3 on 2023-08-01 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_menu_item_description_menu_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_slot',
            new_name='reservation_slot',
        ),
    ]
