# Generated by Django 4.2 on 2023-05-07 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_billsale_products_alter_adddrug_date_of_entering_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 16, 24, 31, 657621), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='9801', max_length=100, verbose_name='رقم الفاتورة'),
        ),
        migrations.AlterField(
            model_name='product_bill',
            name='num_bill',
            field=models.CharField(default='9801', max_length=100, verbose_name='رقم الفاتورة'),
        ),
    ]