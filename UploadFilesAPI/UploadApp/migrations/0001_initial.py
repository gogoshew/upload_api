# Generated by Django 4.0.4 on 2022-05-04 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_org', models.CharField(max_length=200, unique=True, verbose_name='Организация')),
                ('bill_number', models.IntegerField(max_length=15, unique=True, verbose_name='Номер счета клиента')),
                ('bill_sum', models.IntegerField(max_length=200, null=True, verbose_name='Сумма на счете')),
                ('date', models.CharField(max_length=200, unique=True, verbose_name='Организация')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Клиент')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Организация')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='UploadApp.client', unique=True, verbose_name='Клиент')),
            ],
        ),
    ]
