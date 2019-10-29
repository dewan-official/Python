# Generated by Django 2.1.7 on 2019-03-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_candidate_election'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electionId', models.CharField(max_length=20)),
                ('candidateId', models.CharField(max_length=20)),
                ('candidateVOte', models.CharField(max_length=20)),
                ('candidateSign', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Elections',
            fields=[
                ('electionID', models.IntegerField(auto_created=1, primary_key=1000, serialize=False, unique=True)),
                ('electionTitle', models.CharField(max_length=200)),
                ('electionWinner', models.CharField(max_length=20)),
                ('electionStatus', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Election',
        ),
    ]