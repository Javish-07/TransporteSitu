# Generated by Django 4.0.5 on 2022-07-14 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('cooperativa', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('P', 'Publico'), ('E', 'Escolar'), ('T', 'Turistico')], default='F', max_length=1, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('edad', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Pasajero',
                'verbose_name_plural': 'Pasajeros',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cantidad', models.IntegerField()),
                ('fecha_viaje', models.DateTimeField(auto_now_add=True)),
                ('efectivo', models.BooleanField(default=True)),
                ('tipo', models.CharField(choices=[('comodo', 'Comodo'), ('incomodo', 'Incomodo')], default='F', max_length=20)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAdmin.bus')),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAdmin.pasajero')),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': 'Viajes',
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('monto', models.CharField(max_length=30)),
                ('idPasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAdmin.pasajero')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='idTarjeta',
            field=models.ManyToManyField(to='GestionAdmin.pasajero'),
        ),
        migrations.CreateModel(
            name='AccesoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('fecha_viaje', models.DateTimeField(auto_now_add=True)),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAdmin.tarjeta')),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAdmin.viaje')),
            ],
            options={
                'verbose_name': 'AccesoPagos',
            },
        ),
    ]
