# Generated by Django 5.0.6 on 2024-06-23 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gonggu', '0004_alter_item_sellerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
        migrations.AlterField(
            model_name='item',
            name='productImg',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sellerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gonggu.user'),
        ),
    ]
