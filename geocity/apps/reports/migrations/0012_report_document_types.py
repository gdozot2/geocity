# Generated by Django 3.2.15 on 2022-11-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0011_migrate_permits_data"),
    ]

    operations = [
        migrations.RemoveField(model_name="report", name="document_types"),
        migrations.RenameField(
            model_name="report",
            old_name="submissions_document_types",
            new_name="document_types",
        ),
    ]
