# Generated by Django 4.2.5 on 2023-09-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]