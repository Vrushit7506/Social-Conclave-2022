# Generated by Django 4.0.1 on 2022-01-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_delegate_counter_delegate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='counter',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
