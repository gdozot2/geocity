# Generated by Django 3.2.15 on 2022-11-07 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_makeproxymodels'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': '1.5 Champ', 'verbose_name_plural': '1.5 Champs'},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'ordering': ('order',), 'verbose_name': '1.3 Formulaire', 'verbose_name_plural': '1.3 Formulaires'},
        ),
        migrations.AlterModelOptions(
            name='formcategory',
            options={'verbose_name': '1.2 Catégorie', 'verbose_name_plural': '1.2 Catégories'},
        ),
        migrations.AlterModelOptions(
            name='proxyadministrativeentity',
            options={'verbose_name': '1.1 Entité administrative (commune, organisation)', 'verbose_name_plural': '1.1 Entités administratives (commune, organisation)'},
        ),
        migrations.AlterModelOptions(
            name='proxycontacttype',
            options={'verbose_name': '1.6 Contact', 'verbose_name_plural': '1.6 Contacts'},
        ),
    ]
