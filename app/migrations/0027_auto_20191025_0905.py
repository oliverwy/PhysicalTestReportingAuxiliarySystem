# Generated by Django 2.2.6 on 2019-10-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_itemweight'),
    ]

    operations = [
        migrations.CreateModel(
            name='BML',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='序号')),
            ],
        ),
        migrations.AlterField(
            model_name='itemweight',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
    ]
