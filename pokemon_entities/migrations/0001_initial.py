# Generated by Django 2.2.3 on 2020-05-25 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название покемона')),
                ('description', models.TextField(blank=True, default='Нет доступного описания.', verbose_name='Описание покемона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pokemons', verbose_name='Изображение покемона')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Название на английском')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Название на японском')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.Pokemon', verbose_name='Эволюция')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Сила')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Появился в:')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Пропал в:')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('pokemon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.Pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
