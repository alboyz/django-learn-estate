# Generated by Django 4.0 on 2022-01-21 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='User providing the user'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('rater', 'agent')},
        ),
    ]
