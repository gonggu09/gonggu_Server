# Generated by Django 5.0.6 on 2024-06-23 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gonggu', '0003_alter_item_sellerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sellerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellerId', to='gonggu.user'),
        ),
    ]