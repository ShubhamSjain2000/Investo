# Generated by Django 3.1.5 on 2021-04-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='startup',
            field=models.BooleanField(default=False),
        ),
    ]
