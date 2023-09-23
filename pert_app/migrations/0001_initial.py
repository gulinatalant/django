# Generated by Django 4.2.5 on 2023-09-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=60)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]