# Generated by Django 3.2.9 on 2021-12-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210828_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='accounts/profile_pics'),
        ),
    ]