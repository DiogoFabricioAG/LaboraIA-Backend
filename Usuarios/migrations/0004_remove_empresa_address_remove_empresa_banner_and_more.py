# Generated by Django 5.1.5 on 2025-01-28 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='address',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='description',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='web',
        ),
    ]
