# Generated by Django 3.2.13 on 2022-06-16 12:57

import django.contrib.sites.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("permits", "0073_filter_documenttype_for_integrator"),
    ]

    operations = [
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "site_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sites.site",
                    ),
                ),
                (
                    "integrator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="auth.group",
                        verbose_name="Groupe des administrateurs",
                    ),
                ),
            ],
            options={
                "verbose_name": "1.0 Configuration du sous-domaine",
                "verbose_name_plural": "1.0 Configuration des sous-domaines",
            },
            bases=("sites.site",),
            managers=[
                ("objects", django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
