# Generated by Django 3.0.3 on 2020-04-05 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import secrets


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_app', '0004_delete_passwordresetrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=secrets.token_urlsafe, max_length=43)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
