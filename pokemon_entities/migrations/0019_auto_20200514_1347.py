# Generated by Django 2.2.3 on 2020-05-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0018_auto_20200514_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='appeared_at',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='defence',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='disappeared_at',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='health',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='level',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='stamina',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='strength',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Появился в:'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Пропал в:'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сила'),
        ),
    ]
