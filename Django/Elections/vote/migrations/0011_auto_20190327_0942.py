# Generated by Django 2.1.7 on 2019-03-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0010_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='electionId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vote',
            name='userID',
            field=models.IntegerField(),
        ),
    ]