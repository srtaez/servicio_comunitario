# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(default=b'None', upload_to=b'Archivos/')),
                ('descripcion', models.TextField()),
                ('claves', models.TextField()),
                ('autor', models.CharField(max_length=256)),
                ('fuente', models.CharField(max_length=256)),
                ('personas', models.BooleanField(default=False)),
                ('color', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=256)),
                ('ancho', models.CharField(max_length=256)),
                ('largo', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Orientacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orientacion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permisos', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Perspectiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perspectiva', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_archivo', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_imagen', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='catalogo',
            name='categoria',
            field=models.ForeignKey(to='catalogo_app.Categoria'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='orientacion',
            field=models.ForeignKey(default=1, to='catalogo_app.Orientacion'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='permisos',
            field=models.ForeignKey(default=1, to='catalogo_app.Permisos'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='perspectiva',
            field=models.ForeignKey(default=1, to='catalogo_app.Perspectiva'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='tag',
            field=models.ManyToManyField(default=1, to='catalogo_app.Tag'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='tipo_archivo',
            field=models.ForeignKey(default=1, to='catalogo_app.Tipo_Archivo'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='tipo_imagen',
            field=models.ForeignKey(default=1, to='catalogo_app.Tipo_Imagen'),
        ),
    ]
