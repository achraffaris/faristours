# Generated by Django 3.2.2 on 2021-05-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0008_auto_20210519_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='feedbacks',
            field=models.IntegerField(default=0),
        ),
    ]