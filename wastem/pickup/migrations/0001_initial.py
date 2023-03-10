# Generated by Django 4.1.3 on 2023-02-12 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PickupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.CharField(choices=[('B', 'bio-degradable'), ('NB', 'non-biodegradable')], default=None, max_length=25, null=True)),
                ('description', models.CharField(default='none', max_length=200)),
                ('phone_number', models.CharField(default='+91', max_length=20)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickup.location')),
            ],
        ),
    ]
