# Generated by Django 4.2.5 on 2023-10-05 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_categorymodel_alter_productmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categorymodel'),
        ),
    ]