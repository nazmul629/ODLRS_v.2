# Generated by Django 2.2.1 on 2019-07-13 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20190713_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordervalidation',
            old_name='approved_orders',
            new_name='approved_order_by_client',
        ),
    ]
