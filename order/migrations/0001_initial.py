# Generated by Django 4.0 on 2021-12-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255, verbose_name='Order Id')),
                ('total_product_price', models.FloatField(verbose_name='Total Product Price')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
            ],
        ),
    ]