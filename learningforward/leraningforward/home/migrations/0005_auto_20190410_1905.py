# Generated by Django 2.1.4 on 2019-04-10 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_filec_filehtml_filepython'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filec',
            name='fileupload',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])]),
        ),
    ]