# Generated by Django 3.0.2 on 2020-01-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='phoneModel',
            field=models.CharField(default='S8', max_length=255),
            preserve_default=False,
        ),
    ]