# Generated by Django 5.0.6 on 2024-07-23 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_state_voted_ind_state_votes_dem_state_votes_rep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='voted_ind',
            new_name='votes_ind',
        ),
    ]
