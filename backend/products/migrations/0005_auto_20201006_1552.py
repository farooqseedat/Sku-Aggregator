# Generated by Django 3.1.1 on 2020-10-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201006_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sku',
            name='currency',
            field=models.CharField(max_length=100),
        ),
    ]
