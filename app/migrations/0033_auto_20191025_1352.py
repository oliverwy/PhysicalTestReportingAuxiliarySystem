# Generated by Django 2.2.6 on 2019-10-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20191025_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='middledistancerunplustestnormal',
            name='classtype',
        ),
        migrations.RemoveField(
            model_name='oneminutesitupsandpullupplusnormal',
            name='classtype',
        ),
        migrations.AlterField(
            model_name='middledistancerunplustestnormal',
            name='ItemScore',
            field=models.IntegerField(default=0, verbose_name='单项加分值'),
        ),
        migrations.AlterField(
            model_name='oneminutesitupsandpullupplusnormal',
            name='ItemScore',
            field=models.IntegerField(default=0, verbose_name='单项加分值'),
        ),
    ]
