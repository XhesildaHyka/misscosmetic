# Generated by Django 5.1.5 on 2025-03-22 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0021_remove_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestseller_title', models.TextField(blank=True, max_length=450, null=True)),
                ('bestseller_image', models.ImageField(blank=True, null=True, upload_to='bestseller/')),
            ],
        ),
    ]
