# Generated by Django 5.1.5 on 2025-03-15 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0018_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplication.collection'),
        ),
    ]
