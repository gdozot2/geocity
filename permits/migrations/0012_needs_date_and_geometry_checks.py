# Generated by Django 3.1.4 on 2021-01-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0011_works_object_properties_date_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksobjecttype',
            name='needs_date',
            field=models.BooleanField(default=True, verbose_name='avec période de temps'),
        ),
        migrations.AddField(
            model_name='worksobjecttype',
            name='needs_geometry',
            field=models.BooleanField(default=True, verbose_name='avec géométrie'),
        ),
        migrations.AlterField(
            model_name='historicalpermitrequestgeotime',
            name='ends_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date planifiée de fin'),
        ),
        migrations.AlterField(
            model_name='historicalpermitrequestgeotime',
            name='starts_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date planifiée de début'),
        ),
        migrations.AlterField(
            model_name='permitrequestgeotime',
            name='ends_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date planifiée de fin'),
        ),
        migrations.AlterField(
            model_name='permitrequestgeotime',
            name='starts_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date planifiée de début'),
        ),
    ]
