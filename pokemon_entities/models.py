from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField('Название покемона', max_length=200)
    description = models.TextField('Описание покемона', blank=True)
    image = models.ImageField('Изображение покемона', upload_to='pokemons', null=True)
    appeared_at = models.DateTimeField('Появился в:', null=True, blank=True)
    disappeared_at = models.DateTimeField('Пропал в:', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
    title_en = models.CharField('Название на английском', max_length=200, default='', blank=True)
    title_jp = models.CharField('Название на японском', max_length=200, default='', blank=True)
    previous_evolution = models.ForeignKey('self', null=True, blank=True,
                                           on_delete=models.CASCADE,
                                           related_name='next_evolution',
                                           verbose_name='Эволюция')

    def __str__(self):
        if self.id:
            return self.title
        return f'{self.title} (inactive)'


class PokemonEntity(models.Model):
    name = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        null=True, verbose_name='Покемон')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

