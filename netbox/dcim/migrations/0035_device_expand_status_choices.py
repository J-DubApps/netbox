# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0034_rename_module_to_inventoryitem'),
    ]

    # We convert the BooleanField to an IntegerField first as PostgreSQL does not provide a direct cast for boolean to
    # smallint (attempting to convert directly yields the error "cannot cast type boolean to smallint").
    operations = [
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.PositiveIntegerField(choices=[[1, b'Active'], [0, b'Offline'], [2, b'Planned'], [3, b'Staged'], [4, b'Failed'], [5, b'Inventory']], default=1, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[[1, b'Active'], [0, b'Offline'], [2, b'Planned'], [3, b'Staged'], [4, b'Failed'], [5, b'Inventory']], default=1, verbose_name=b'Status'),
        ),
    ]