# Generated by Django 3.2.5 on 2022-01-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20220111_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='csv',
            field=models.FileField(upload_to='db/csv'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='name',
            field=models.FileField(upload_to='db/name'),
        ),
    ]
