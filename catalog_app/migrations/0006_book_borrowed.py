# Generated by Django 3.0.3 on 2020-04-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_remove_bookinstance_imprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
    ]
