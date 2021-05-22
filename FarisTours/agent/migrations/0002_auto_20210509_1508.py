# Generated by Django 3.2.2 on 2021-05-09 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='tour',
            name='seats',
        ),
        migrations.AddField(
            model_name='tour',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tour',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='views',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tourdate',
            name='seats',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tour',
            name='thumbnail',
            field=models.ImageField(default='1.jpg', upload_to='Thumbnails'),
        ),
        migrations.AlterField(
            model_name='tourdate',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tourgallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallerry'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.FloatField(default=0.0)),
                ('comment', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('pp', 'PayPal'), ('cc', 'Credit Card'), ('bt', 'Bank Transfer')], default='bt', max_length=2)),
                ('status', models.CharField(max_length=100)),
                ('transaction', models.CharField(max_length=200)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='agent.bookingorders')),
            ],
        ),
        migrations.AddField(
            model_name='bookingorders',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='agent.payment'),
        ),
        migrations.AddField(
            model_name='bookingorders',
            name='planning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.tourdate'),
        ),
    ]
