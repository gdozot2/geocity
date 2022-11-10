# Generated by Django 3.2.15 on 2022-10-13 11:45

from django.db import migrations

from geocity.migrations import (
    common_fields_values,
    copy_tags,
    migrate_contenttypes,
    sync_sequence,
)


def create_administrative_entities(apps, schema_editor):
    PermitAdministrativeEntity = apps.get_model("permits", "PermitAdministrativeEntity")
    AdministrativeEntity = apps.get_model("accounts", "AdministrativeEntity")

    for administrative_entity in PermitAdministrativeEntity.objects.all():
        new_administrative_entity = AdministrativeEntity.objects.create(
            **common_fields_values(PermitAdministrativeEntity, administrative_entity)
        )

        copy_tags(
            apps,
            from_obj=administrative_entity,
            to_obj=new_administrative_entity,
        )
        new_administrative_entity.sites.set(administrative_entity.sites.all())


def create_user_profiles(apps, schema_editor):
    PermitAuthor = apps.get_model("permits", "PermitAuthor")
    UserProfile = apps.get_model("accounts", "UserProfile")

    for permit_author in PermitAuthor.objects.all():
        UserProfile.objects.create(**common_fields_values(UserProfile, permit_author))


def create_historical_user_profiles(apps, schema_editor):
    HistoricalPermitAuthor = apps.get_model("permits", "HistoricalPermitAuthor")
    HistoricalUserProfile = apps.get_model("accounts", "HistoricalUserProfile")

    for historical_permit_author in HistoricalPermitAuthor.objects.all():
        HistoricalUserProfile.objects.create(
            **common_fields_values(HistoricalUserProfile, historical_permit_author)
        )


def create_permit_departments(apps, schema_editor):
    PermitDepartment = apps.get_model("permits", "PermitDepartment")
    AccountsPermitDepartment = apps.get_model("accounts", "PermitDepartment")

    for permit_department in PermitDepartment.objects.all():
        AccountsPermitDepartment.objects.create(
            **common_fields_values(AccountsPermitDepartment, permit_department)
        )


def create_site_profiles(apps, schema_editor):
    SiteProfile = apps.get_model("permits", "SiteProfile")
    AccountsSiteProfile = apps.get_model("accounts", "SiteProfile")

    for site_profile in SiteProfile.objects.all():
        AccountsSiteProfile.objects.create(
            **common_fields_values(AccountsSiteProfile, site_profile)
        )


def create_template_customizations(apps, schema_editor):
    TemplateCustomization = apps.get_model("permits", "TemplateCustomization")
    AccountsTemplateCustomization = apps.get_model("accounts", "TemplateCustomization")

    for template_customization in TemplateCustomization.objects.all():
        AccountsTemplateCustomization.objects.create(
            **common_fields_values(
                AccountsTemplateCustomization, template_customization
            )
        )


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_permitdepartment_shortname"),
        ("permits", "0084_add_shortname_and_change_text"),
    ]

    operations = [
        migrations.RunPython(migrate_contenttypes),
        migrations.RunPython(create_administrative_entities),
        sync_sequence("accounts_administrativeentity"),
        migrations.RunPython(create_user_profiles),
        sync_sequence("accounts_userprofile"),
        migrations.RunPython(create_historical_user_profiles),
        sync_sequence("accounts_historicaluserprofile", "history_id"),
        migrations.RunPython(create_permit_departments),
        sync_sequence("accounts_permitdepartment"),
        migrations.RunPython(create_site_profiles),
        sync_sequence("accounts_siteprofile"),
        migrations.RunPython(create_template_customizations),
        sync_sequence("accounts_templatecustomization"),
    ]
