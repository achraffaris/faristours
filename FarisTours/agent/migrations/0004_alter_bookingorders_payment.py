# Generated by Django 3.2.2 on 2021-05-10 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_auto_20210509_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingorders',
            name='payment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='agent.payment'),
        ),
    ]
