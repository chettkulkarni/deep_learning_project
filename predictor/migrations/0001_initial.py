# Generated by Django 3.0.5 on 2020-05-10 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adName', models.CharField(max_length=200)),
                ('adContent', models.TextField(max_length=200)),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictor.AdvertisementCategory')),
            ],
        ),
    ]
