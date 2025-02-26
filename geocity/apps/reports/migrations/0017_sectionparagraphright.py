# Generated by Django 4.1.4 on 2022-12-15 14:20

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0016_change_admin_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="SectionParagraphRight",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, default="", max_length=2000, verbose_name="Titre"
                    ),
                ),
                (
                    "content",
                    ckeditor.fields.RichTextField(
                        help_text='Il est possible d\'inclure des variables et de la logique avec la <a href="https://jinja.palletsprojects.com/en/3.1.x/templates/">syntaxe Jinja</a>. Les variables de la demande sont accessible dans `{{request_data}}` et celles du formulaire dans `{{form_data}}`.',
                        verbose_name="Contenu",
                    ),
                ),
            ],
            options={
                "verbose_name": "Paragraphe libre aligné à droite",
            },
            bases=("reports.section",),
        ),
    ]
