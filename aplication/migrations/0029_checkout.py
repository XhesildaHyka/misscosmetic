# Generated by Django 5.1.5 on 2025-04-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0028_cart_user_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=450)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
