# Generated by Django 4.0.1 on 2022-02-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_delegate_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='Paid',
            field=models.BooleanField(default=False),
        ),
    ]
