# Generated by Django 4.1.3 on 2022-11-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PiState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoadState', models.IntegerField(null=True)),
                ('LightState', models.IntegerField(null=True)),
            ],
        ),
    ]