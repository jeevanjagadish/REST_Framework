# Generated by Django 3.0.2 on 2020-02-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('Technology', models.CharField(max_length=100)),
                ('company_size', models.IntegerField()),
                ('company_ceo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('phoneno', models.IntegerField()),
            ],
        ),
    ]