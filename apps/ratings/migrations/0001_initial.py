# Generated by Django 4.0 on 2022-01-15 18:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_profile_num_reviews'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('craeted_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(choices=[(1, 'poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excelent')], default=0, help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good 5=Excelent', verbose_name='Rating')),
                ('argument', models.TextField(verbose_name='Comment')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_review', to='profiles.profile', verbose_name='Agent being rated')),
                ('rater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='User providing the user')),
            ],
            options={
                'unique_together': {('rater', 'agent')},
            },
        ),
    ]
