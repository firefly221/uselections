# Generated by Django 5.0.6 on 2024-07-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_voter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]