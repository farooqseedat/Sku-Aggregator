# Generated by Django 3.1.1 on 2020-10-05 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201005_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(max_length=100),
        ),
    ]
