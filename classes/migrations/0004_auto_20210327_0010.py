# Generated by Django 3.1.7 on 2021-03-27 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20210325_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
