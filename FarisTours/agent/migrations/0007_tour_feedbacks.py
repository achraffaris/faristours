# Generated by Django 3.2.2 on 2021-05-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0006_auto_20210511_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='feedbacks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]