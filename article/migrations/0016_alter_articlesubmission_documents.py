# Generated by Django 3.2.6 on 2021-09-05 09:38

import article.models
import article.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_alter_articlesubmission_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesubmission',
            name='documents',
            field=models.FileField(upload_to=article.models.ArticleSubmission.get_hashed_file_path, validators=[article.validators.validate_file_size]),
        ),
    ]
