# Generated by Django 4.0.1 on 2022-01-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_delegate_counter_alter_delegate_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='id',
        ),
    ]
