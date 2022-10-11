# Generated by Django 4.0.5 on 2022-10-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListaWeb2Tri', '0002_alter_habilitacao_validadehab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corgercor',
            name='cpfGerenciado',
        ),
        migrations.RemoveField(
            model_name='corgercor',
            name='cpfGerenciador',
        ),
        migrations.AddField(
            model_name='corgercor',
            name='corretores',
            field=models.ManyToManyField(related_name='CorGerCor', to='ListaWeb2Tri.corretor'),
        ),
    ]
