# Generated by Django 5.0.6 on 2024-07-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('education', models.CharField(choices=[('HS', 'High school'), ('C', 'College')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]