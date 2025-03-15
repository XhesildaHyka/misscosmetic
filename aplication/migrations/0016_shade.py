# Generated by Django 5.1.5 on 2025-03-15 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0015_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color_code', models.CharField(blank=True, max_length=7, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shades', to='aplication.product')),
            ],
        ),
    ]
