# Generated by Django 4.0 on 2024-09-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schapp', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
