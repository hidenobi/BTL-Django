# Generated by Django 4.0.1 on 2024-05-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
