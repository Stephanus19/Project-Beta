# Generated by Django 4.0.3 on 2023-01-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobileVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_href', models.CharField(max_length=100, null=True, unique=True)),
                ('color', models.CharField(max_length=50, null=True)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('vin', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_number', models.PositiveSmallIntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.PositiveSmallIntegerField(max_length=17, unique=True)),
                ('vip', models.BooleanField(default=False)),
                ('customer_name', models.CharField(max_length=200, null=True, unique=True)),
                ('start_date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('reason', models.CharField(max_length=200)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='service_rest.technician')),
            ],
        ),
    ]
