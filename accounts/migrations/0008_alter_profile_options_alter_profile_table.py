# Generated by Django 4.2.6 on 2023-10-17 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['username'], 'verbose_name': 'User'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='user_profile',
        ),
    ]
