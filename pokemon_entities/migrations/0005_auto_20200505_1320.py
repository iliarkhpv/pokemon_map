# Generated by Django 2.2.3 on 2020-05-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='appeared_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='disappeared_at',
            field=models.DateTimeField(null=True),
        ),
    ]