# Generated by Django 3.2.6 on 2021-08-30 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210828_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-datetime']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='datetime',
        ),
    ]
