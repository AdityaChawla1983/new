# Generated by Django 3.1.7 on 2021-06-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='designation',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='mainphoto',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]