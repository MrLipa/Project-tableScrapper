# Generated by Django 3.2.5 on 2022-01-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0004_alter_scrap_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='csv',
            field=models.FileField(max_length=200, upload_to='db/csv'),
        ),
    ]
