# Generated by Django 5.0.6 on 2024-06-18 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_cancha_favorito'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancha',
            name='favorito',
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id_favorito', models.AutoField(primary_key=True, serialize=False)),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.cancha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='RedeSocial',
        ),
    ]
