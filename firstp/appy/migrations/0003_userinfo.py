# Generated by Django 4.1.3 on 2023-06-01 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_alter_drums_phoneno_alter_guitar_phoneno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('Name', models.CharField(max_length=500)),
                ('Phoneno', models.IntegerField(primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=500)),
                ('Passwd', models.CharField(max_length=500)),
            ],
        ),
    ]
