# Generated by Django 4.2.6 on 2023-10-17 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['username'], 'verbose_name': 'user_profile'},
        ),
    ]
