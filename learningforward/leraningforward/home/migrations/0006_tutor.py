# Generated by Django 2.1.4 on 2019-04-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190410_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorname', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('emailid', models.CharField(default='', max_length=40)),
                ('phoneno', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]