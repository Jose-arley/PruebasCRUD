# Generated by Django 3.0.2 on 2021-05-18 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name_client', models.CharField(max_length=100)),
                ('user_createc', models.DateField()),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('Update', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prueba.Categorias')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.Ciudades')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prueba.Paises')),
            ],
        ),
    ]