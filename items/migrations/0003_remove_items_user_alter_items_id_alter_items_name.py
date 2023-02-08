# Generated by Django 4.1.5 on 2023-02-07 11:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_items_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='user',
        ),
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
    ]
