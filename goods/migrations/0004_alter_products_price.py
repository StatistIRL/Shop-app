# Generated by Django 4.2.11 on 2024-03-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Цена'),
        ),
    ]
