# Generated by Django 4.2.5 on 2023-11-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_orderemployee_order_orderuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeJobTitle',
            field=models.TextField(choices=[('АД', 'Администратор'), ('МД', 'Менеджер доставок')]),
        ),
    ]
