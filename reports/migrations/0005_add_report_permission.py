# Generated by Django 3.2.13 on 2022-06-28 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_reportlayout_background'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'permissions': [('can_generate_pdf', 'Générer des documents pdf')], 'verbose_name': '5.2 Configuration du rapport', 'verbose_name_plural': '5.2 Configuration des rapports'},
        ),
    ]
