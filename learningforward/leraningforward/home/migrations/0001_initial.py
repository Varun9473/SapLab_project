# Generated by Django 2.1.4 on 2019-04-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50, unique=True)),
                ('messages', models.CharField(max_length=500)),
            ],
        ),
    ]
