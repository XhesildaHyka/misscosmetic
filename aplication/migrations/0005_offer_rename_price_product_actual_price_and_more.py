# Generated by Django 5.1.5 on 2025-03-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0004_accessor_arrival_contact_makeup_marka_skincare_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='actual_price',
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
