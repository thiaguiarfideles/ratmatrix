# Generated by Django 4.1.7 on 2023-04-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rat_s', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cod Conselho'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
