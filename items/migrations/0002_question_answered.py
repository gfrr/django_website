# Generated by Django 2.0 on 2017-06-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
