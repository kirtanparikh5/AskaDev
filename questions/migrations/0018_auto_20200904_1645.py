# Generated by Django 2.2.6 on 2020-09-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_auto_20200904_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='url',
            field=models.CharField(default='01452f606daacca3bc5a214273d681cd816265d2', max_length=32),
        ),
    ]
