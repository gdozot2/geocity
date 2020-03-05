# Generated by Django 2.2.6 on 2020-03-05 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0029_auto_20191115_0801'),
        ('permits', '0004_add_actors_through'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermitActorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Autres'), (2, 'Popriétaire'), (3, 'Entreprise'), (4, "Maître d'ouvrage"), (1, "Requérant si différent de l'auteur de la demande"), (5, 'Sécurité'), (6, 'Association')], default=0, verbose_name='type de contact')),
                ('works_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_contact_types', to='permits.WorksType', verbose_name='type de travaux')),
            ],
            options={
                'verbose_name': 'contact à saisir',
                'verbose_name_plural': 'contacts à saisir',
            },
        ),
    ]
