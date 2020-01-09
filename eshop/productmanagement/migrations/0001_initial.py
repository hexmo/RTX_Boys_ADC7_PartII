# Generated by Django 3.0.2 on 2020-01-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('stockNo', models.IntegerField()),
                ('releaseDate', models.DateField()),
                ('specs', models.FileField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=255)),
                ('screenSize', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=60)),
                ('RAM', models.CharField(max_length=255)),
                ('ROM', models.CharField(max_length=255)),
                ('battery', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name', 'price', 'stockNo', 'releaseDate', 'specs', 'brand'],
                'abstract': False,
            },
        ),
    ]
