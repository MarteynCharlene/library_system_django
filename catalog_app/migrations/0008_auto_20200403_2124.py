# Generated by Django 3.0.3 on 2020-04-03 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog_app', '0007_auto_20200403_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTracker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('borrowed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['due_back'],
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='borrowed',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='name',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='book_pics'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='magazine_image',
            field=models.ImageField(default='default.jpg', upload_to='magazine_pics'),
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='booktracker',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog_app.Book'),
        ),
        migrations.AddField(
            model_name='booktracker',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]