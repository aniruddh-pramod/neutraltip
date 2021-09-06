# Generated by Django 3.2.6 on 2021-09-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_alter_articlesubmission_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesubmission',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=50),
        ),
    ]