# Generated by Django 3.2.15 on 2022-10-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListaWeb2Tri', '0004_alter_corgercor_corretores'),
    ]

    operations = [
        migrations.AddField(
            model_name='corretor',
            name='corretores',
            field=models.ManyToManyField(to='ListaWeb2Tri.Corretor'),
        ),
    ]
