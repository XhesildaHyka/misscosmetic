# Generated by Django 5.1.5 on 2025-03-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0014_remove_product_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
    ]
