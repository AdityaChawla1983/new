# Generated by Django 3.1.7 on 2021-06-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210620_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='mainphoto',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%M/%D/'),
        ),
    ]
