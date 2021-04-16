# Generated by Django 3.2 on 2021-04-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='dojo_city',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dojo',
            name='dojo_state',
            field=models.CharField(default='Location', max_length=255),
            preserve_default=False,
        ),
    ]
