# Generated by Django 4.0.5 on 2022-06-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='data publisehd')),
                ('body', models.TextField()),
                ('writer', models.CharField(max_length=20)),
                ('feeling_of_today', models.TextField(max_length=100)),
            ],
        ),
    ]
