# Generated by Django 4.0.1 on 2022-01-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_remove_delegate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='TnC',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
