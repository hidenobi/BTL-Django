# Generated by Django 4.0.1 on 2024-03-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='completed',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
