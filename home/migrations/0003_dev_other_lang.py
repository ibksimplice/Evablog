# Generated by Django 3.2.7 on 2021-09-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dev_tagjob_taglag_taglevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='other_lang',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
