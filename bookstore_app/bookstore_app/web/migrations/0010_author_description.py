# Generated by Django 4.0.3 on 2022-04-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
