# Generated by Django 2.2.3 on 2020-05-06 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_pokemon_evalution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='evalution',
            new_name='previous_evolution',
        ),
    ]
