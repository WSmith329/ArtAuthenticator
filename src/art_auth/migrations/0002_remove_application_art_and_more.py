# Generated by Django 4.2.5 on 2023-09-19 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='art',
        ),
        migrations.RemoveField(
            model_name='application',
            name='authentication',
        ),
        migrations.AddField(
            model_name='art',
            name='application',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='art_auth.application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authentication',
            name='application',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='art_auth.application'),
            preserve_default=False,
        ),
    ]
