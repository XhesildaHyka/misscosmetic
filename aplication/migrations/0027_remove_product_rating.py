# Generated by Django 5.1.5 on 2025-03-22 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0026_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
