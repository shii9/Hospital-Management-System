# Generated by Django 5.1.2 on 2024-11-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0008_rename_wordboy_wardboy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
