# Generated by Django 5.1.5 on 2025-04-01 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0038_order_full_name_order_payment_method_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_at_time_of_order', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='aplication.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplication.product')),
            ],
        ),
    ]
