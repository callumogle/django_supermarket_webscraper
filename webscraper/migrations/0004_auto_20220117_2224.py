# Generated by Django 3.2.8 on 2022-01-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0003_alter_asdascrape_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asdascrape',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='asdascrape',
            name='unit_price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
