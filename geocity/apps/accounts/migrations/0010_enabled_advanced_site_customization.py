# Generated by Django 4.1.4 on 2023-01-26 15:29

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_siteprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatecustomization',
            name='background_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Couleur de fond'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='contact_url',
            field=models.URLField(blank=True, max_length=512, verbose_name='Lien vers le moyen de contact'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='enable_geocalendar',
            field=models.BooleanField(default=False, verbose_name="Définit si l'application du calendrier cartographique est utilisée"),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='general_conditions_url',
            field=models.URLField(blank=True, max_length=512, verbose_name='Lien vers les conditions générales'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='geocalendar_url',
            field=models.URLField(blank=True, max_length=512, verbose_name="URL de l'application calendrier cartographique"),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='login_background_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Couleur de fond du login'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='max_file_upload_size',
            field=models.IntegerField(default=10485760, help_text='Taille maximum des fichiers uploadés', verbose_name='Taille maximum des fichiers uploadés'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='primary_color',
            field=colorfield.fields.ColorField(default='#008c6f', image_field=None, max_length=18, samples=None, verbose_name='Couleur primaire'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='privacy_policy_url',
            field=models.URLField(blank=True, max_length=512, verbose_name='Lien vers la politique de confidentialité'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='secondary_color',
            field=colorfield.fields.ColorField(default='#01755d', image_field=None, max_length=18, samples=None, verbose_name='Couleur secondaire'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='table_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None, verbose_name='Couleur du tableau'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='text_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None, verbose_name='Couleur du texte'),
        ),
        migrations.AddField(
            model_name='templatecustomization',
            name='title_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None, verbose_name='Couleur du titre'),
        ),
    ]
