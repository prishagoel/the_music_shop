# Generated by Django 4.1.3 on 2023-05-31 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drums',
            name='Phoneno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='Phoneno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='piano',
            name='Phoneno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='violin',
            name='Phoneno',
            field=models.IntegerField(),
        ),
    ]
