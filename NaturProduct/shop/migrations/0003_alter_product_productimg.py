# Generated by Django 4.2.7 on 2023-11-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImg',
            field=models.FileField(upload_to='static/img/prodImg'),
        ),
    ]