# Generated by Django 4.1.3 on 2022-11-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_media_company_alter_media_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='duration'),
        ),
    ]