# Generated by Django 4.0.1 on 2024-05-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]