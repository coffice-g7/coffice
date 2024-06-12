# Generated by Django 5.0.4 on 2024-06-06 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_favorite'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('duration', models.IntegerField(help_text='Duração em minutos')),
                ('num_people', models.IntegerField()),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('C', 'Confirmada'), ('X', 'Cancelada')], default='P', max_length=1)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.coffee_shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
