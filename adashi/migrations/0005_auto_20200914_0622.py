# Generated by Django 3.1 on 2020-09-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adashi', '0004_join'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='position',
            new_name='spinner_position',
        ),
        migrations.AlterField(
            model_name='join',
            name='spinned',
            field=models.BooleanField(default=True),
        ),
    ]
