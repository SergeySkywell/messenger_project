# Generated by Django 4.2.8 on 2023-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_app', '0005_remove_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]