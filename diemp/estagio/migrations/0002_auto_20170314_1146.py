# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-14 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagio',
            name='estado',
            field=models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Terminado', 'Terminado'), ('Aguardando Documentos', 'Aguardando Documentos'), ('Termo Aditivo', 'Termo Aditivo'), ('Cancelado', 'Cancelado')], db_column='Estado', max_length=150),
        ),
    ]
