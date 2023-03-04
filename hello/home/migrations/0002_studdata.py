# Generated by Django 4.1.7 on 2023-03-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=128)),
                ('sid', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('parphone', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=8)),
                ('sem', models.CharField(max_length=1)),
                ('date', models.DateField()),
            ],
        ),
    ]
