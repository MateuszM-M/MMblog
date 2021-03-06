# Generated by Django 3.1.1 on 2020-10-09 13:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201006_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
    ]
