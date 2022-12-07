# Generated by Django 4.1.3 on 2022-12-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_alter_castcrew_media_alter_season_media'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='castcrew',
            options={'verbose_name': 'cast_crew', 'verbose_name_plural': 'cast_crew'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['country'], 'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='episode',
            options={'verbose_name': 'episode', 'verbose_name_plural': 'episodes'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['country'], 'verbose_name': 'location', 'verbose_name_plural': 'locations'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'media'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'season', 'verbose_name_plural': 'seasons'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='media',
            name='company',
            field=models.ManyToManyField(blank=True, related_name='medias', to='movie_app.company', verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='media',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='medias', to='movie_app.genre', verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='media',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='medias', to='movie_app.language', verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='media',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='medias', to='movie_app.location', verbose_name='location'),
        ),
    ]
