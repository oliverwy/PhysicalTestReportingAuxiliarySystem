# Generated by Django 2.2.6 on 2019-10-21 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191021_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='enter_date',
            new_name='enrollment',
        ),
    ]
