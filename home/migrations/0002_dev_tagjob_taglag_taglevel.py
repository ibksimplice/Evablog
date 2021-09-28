# Generated by Django 3.2.7 on 2021-09-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Taglag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_lang', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Taglevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('Describe_yourself', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('profile_pic', models.FileField(upload_to='images/')),
                ('Level_of_seniority', models.ManyToManyField(to='home.Taglevel')),
                ('lang', models.ManyToManyField(to='home.Taglag')),
            ],
        ),
    ]