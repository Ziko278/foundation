# Generated by Django 4.1.1 on 2022-12-22 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0005_siteaboutinfomodel_alter_siteheromodel_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteaboutinfomodel',
            old_name='name',
            new_name='title',
        ),
    ]
