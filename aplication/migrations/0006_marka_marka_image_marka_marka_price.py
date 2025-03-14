# Generated by Django 5.1.7 on 2025-03-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0005_offer_rename_price_product_actual_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marka',
            name='marka_image',
            field=models.ImageField(blank=True, null=True, upload_to='marka/'),
        ),
        migrations.AddField(
            model_name='marka',
            name='marka_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
