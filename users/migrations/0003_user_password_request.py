# Generated by Django 3.1.7 on 2021-03-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210324_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_request',
            field=models.BooleanField(default=False),
        ),
    ]