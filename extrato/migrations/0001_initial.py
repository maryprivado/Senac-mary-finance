# Generated by Django 4.2.4 on 2023-08-30 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.categoria')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.conta')),
            ],
        ),
    ]
