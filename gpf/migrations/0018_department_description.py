# Generated by Django 2.1.5 on 2019-02-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0017_remove_department_email_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.CharField(default='Service', max_length=100, verbose_name='description'),
        ),
    ]
