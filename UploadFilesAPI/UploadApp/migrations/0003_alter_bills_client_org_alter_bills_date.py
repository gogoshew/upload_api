# Generated by Django 4.0.4 on 2022-05-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UploadApp', '0002_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='client_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='UploadApp.organization', unique=True, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='date',
            field=models.DateField(verbose_name='Дата открытия счета'),
        ),
    ]
