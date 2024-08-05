# Generated by Django 5.0.6 on 2024-07-23 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_voter_voted'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.CharField(choices=[('Republican', 'Republican'), ('Democrat', 'Democrat'), ('Independent', 'Independent')], max_length=50),
        ),
        migrations.AlterField(
            model_name='voter',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state'),
        ),
    ]