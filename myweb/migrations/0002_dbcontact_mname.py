# Generated by Django 4.2.3 on 2023-07-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbcontact',
            name='mname',
            field=models.CharField(default='Reena', max_length=50),
            preserve_default=False,
        ),
    ]