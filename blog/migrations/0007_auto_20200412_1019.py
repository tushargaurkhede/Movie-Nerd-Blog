# Generated by Django 3.0.5 on 2020-04-12 04:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200412_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular comment', primary_key=True, serialize=False),
        ),
    ]