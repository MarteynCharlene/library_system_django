# Generated by Django 3.0.3 on 2020-03-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_auto_20200330_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
