# Generated by Django 2.2.3 on 2020-05-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20200514_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]