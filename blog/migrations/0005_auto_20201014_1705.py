# Generated by Django 3.1.1 on 2020-10-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]