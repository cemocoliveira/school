# Generated by Django 3.1.7 on 2021-03-25 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('turno', models.CharField(choices=[('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.IntegerField(choices=[(1, 'SEG'), (2, 'TER'), (3, 'QUA'), (4, 'QUI'), (5, 'SEX'), (6, 'SAB'), (7, 'DOM')])),
                ('inicio', models.TimeField()),
                ('termino', models.TimeField()),
                ('disciplina', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=100)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.turma')),
            ],
        ),
    ]