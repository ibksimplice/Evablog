# Generated by Django 3.2.7 on 2021-09-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_dev_other_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='Job',
            field=models.ManyToManyField(default='fulltime', to='home.Tagjob'),
        ),
    ]