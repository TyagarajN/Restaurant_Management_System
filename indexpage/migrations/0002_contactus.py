# Generated by Django 4.0.4 on 2022-05-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
