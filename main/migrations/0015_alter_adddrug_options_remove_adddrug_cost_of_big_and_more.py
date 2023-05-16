# Generated by Django 4.2 on 2023-05-07 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_billsale_products_product_bill_num_bill_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adddrug',
            options={'verbose_name': 'drug', 'verbose_name_plural': 'drugs'},
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='cost_of_big',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='cost_of_medium',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='cost_of_small',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='num_of_big_medium',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='num_of_big_unit',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='num_of_medium_small',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='num_of_medium_unit',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='num_of_small_unit',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='price_of_big',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='price_of_medium',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='price_of_small',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='unit_big',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='unit_medium',
        ),
        migrations.RemoveField(
            model_name='adddrug',
            name='unit_small',
        ),
        migrations.AddField(
            model_name='adddrug',
            name='cost_of_unit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تكلفة الوحدة'),
        ),
        migrations.AddField(
            model_name='adddrug',
            name='num_of_unit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='عدد الوحدات'),
        ),
        migrations.AddField(
            model_name='adddrug',
            name='price_of_unit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='سعر الوحدة'),
        ),
        migrations.AddField(
            model_name='adddrug',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='الوحدة'),
        ),
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 13, 16, 4, 737122), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='3034', max_length=100, verbose_name='رقم الفاتورة'),
        ),
        migrations.AlterField(
            model_name='product_bill',
            name='num_bill',
            field=models.CharField(default='3034', max_length=100, verbose_name='رقم الفاتورة'),
        ),
    ]
