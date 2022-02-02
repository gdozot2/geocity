# Generated by Django 3.2.7 on 2022-01-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0055_fix_typo'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpermitauthor',
            name='notify_per_email',
            field=models.BooleanField(default=True, verbose_name='Me notifier par e-mail'),
        ),
        migrations.AddField(
            model_name='permitauthor',
            name='notify_per_email',
            field=models.BooleanField(default=True, verbose_name='Me notifier par e-mail'),
        ),
    ]
