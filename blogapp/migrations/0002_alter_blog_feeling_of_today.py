# Generated by Django 4.0.5 on 2022-06-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='feeling_of_today',
            field=models.TextField(),
        ),
    ]
