# Generated by Django 3.1.1 on 2020-10-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201014_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='acitve',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(max_length=2000),
        ),
    ]
