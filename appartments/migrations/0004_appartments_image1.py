# Generated by Django 3.1.4 on 2020-12-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartments', '0003_auto_20201222_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartments',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='appartments'),
        ),
    ]
