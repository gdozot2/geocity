# Generated by Django 3.2.13 on 2022-06-09 13:37

from django.db import migrations, models
import django.db.models.deletion
import streamfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('permits', '0072_filter_documenttype_for_integrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('width', models.PositiveIntegerField(default=210)),
                ('height', models.PositiveIntegerField(default=297)),
                ('margin_top', models.PositiveIntegerField(default=10)),
                ('margin_right', models.PositiveIntegerField(default=10)),
                ('margin_bottom', models.PositiveIntegerField(default=10)),
                ('margin_left', models.PositiveIntegerField(default=10)),
                ('font', models.CharField(blank=True, help_text='La liste des polices disponbiles est visible sur <a href="https://fonts.google.com/" target="_blank">Goole Fonts</a>', max_length=1024, null=True)),
                ('background', models.ImageField(blank=True, help_text='Image d\'arrière plan ("papier à en-tête")', null=True, upload_to='')),
                ('integrator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Groupe des administrateurs')),
            ],
            options={
                'verbose_name': "5.1 Configuration du modèle d'impression de rapport",
                'verbose_name_plural': "5.1 Configuration des modèles d'impression de rapport",
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('stream', streamfield.fields.StreamField(blank=True, default='[]')),
                ('integrator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Groupe des administrateurs')),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='reports.reportlayout')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='permits.complementarydocumenttype')),
                ('work_object_types', models.ManyToManyField(related_name='reports', to='permits.WorksObjectType')),
            ],
            options={
                'verbose_name': '5.2 Configuration du rapport',
                'verbose_name_plural': '5.2 Configuration des rapports',
            },
        ),
    ]
