# Generated by Django 5.1.2 on 2024-11-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0009_alter_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wardboy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
