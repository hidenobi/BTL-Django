# Generated by Django 4.0.1 on 2024-05-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
