# Generated by Django 4.2.1 on 2023-06-14 11:23

from django.db import migrations, models

from geocity.apps.api.services import convert_string_to_api_key


class Migration(migrations.Migration):
    def api_name_from_name(apps, schema_editor):

        SubmissionAmendField = apps.get_model("submissions", "SubmissionAmendField")

        for amend_field in SubmissionAmendField.objects.all():
            amend_field.api_name = convert_string_to_api_key(amend_field.name)
            amend_field.save(update_fields=["api_name"])

    dependencies = [
        ("submissions", "0019_datamigration_sent_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="submissionamendfield",
            name="help_text",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="information complémentaire"
            ),
        ),
        migrations.AddField(
            model_name="submissionamendfield",
            name="placeholder",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="exemple de donnée à saisir"
            ),
        ),
        migrations.AddField(
            model_name="submissionamendfield",
            name="regex_pattern",
            field=models.CharField(
                blank=True,
                help_text="Exemple: ^[0-9]{4}$",
                max_length=255,
                verbose_name="regex pattern",
            ),
        ),
        migrations.AddField(
            model_name="submissionamendfield",
            name="api_name",
            field=models.CharField(
                blank=True,
                help_text="Se génère automatiquement lorsque celui-ci est vide.",
                max_length=255,
                verbose_name="Nom dans l'API",
            ),
        ),
        migrations.RunPython(api_name_from_name),
    ]
