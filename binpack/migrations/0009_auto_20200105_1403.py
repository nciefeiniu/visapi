# Generated by Django 2.2.7 on 2020-01-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binpack', '0008_result_n_tiles_placed'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='their_id',
            field=models.IntegerField(blank=True, help_text='ID from external dataset.', null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='n_tiles_placed',
            field=models.IntegerField(blank=True, help_text='Number of tiles placed before a solution was found', null=True),
        ),
    ]
