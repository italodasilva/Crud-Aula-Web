# Generated by Django 4.0.5 on 2022-09-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListaWeb2Tri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilitacao',
            name='validadeHab',
            field=models.CharField(max_length=14),
        ),
    ]
