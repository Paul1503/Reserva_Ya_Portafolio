# Generated by Django 5.0.6 on 2024-07-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_reserva_estado_pago_reserva_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id_banco', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
            ],
        ),
    ]
