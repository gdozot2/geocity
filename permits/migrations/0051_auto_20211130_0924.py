# Generated by Django 3.2.7 on 2021-11-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0050_fix_regex_for_administrative_entity_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qgisproject',
            name='qgis_atlas_coverage_layer',
        ),
        migrations.AlterField(
            model_name='qgisproject',
            name='qgis_layers',
            field=models.CharField(max_length=500, verbose_name="Couches séparées par des ','. 'permits' est OBLIGATOIRE ici et dans le projet QGIS"),
        ),
    ]
