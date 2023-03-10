# Generated by Django 4.1.1 on 2022-12-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0006_rename_name_siteaboutinfomodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CauseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='images/hero')),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], max_length=20)),
                ('goal', models.FloatField()),
                ('raised', models.FloatField(default=0)),
            ],
        ),
    ]
