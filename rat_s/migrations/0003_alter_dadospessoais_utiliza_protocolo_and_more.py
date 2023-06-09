# Generated by Django 4.1.7 on 2023-04-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rat_s', '0002_alter_dadospessoais_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='utiliza_protocolo',
            field=models.IntegerField(choices=[(1, 'SIM'), (2, 'NÃO')], null=True, verbose_name='Utiliza protocolo gerenciavel ?'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='utiliza_rotina',
            field=models.IntegerField(choices=[(1, 'SIM'), (2, 'NÃO')], null=True, verbose_name='Utiliza rotina ?'),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='utiliza_rotina_especial',
            field=models.IntegerField(choices=[(1, 'SIM'), (2, 'NÃO')], null=True, verbose_name='Utiliza rotina especial ?'),
        ),
    ]
