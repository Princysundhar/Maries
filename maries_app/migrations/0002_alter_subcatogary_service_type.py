# Generated by Django 3.2.23 on 2023-11-10 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maries_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcatogary',
            name='SERVICE_TYPE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maries_app.service_type'),
        ),
    ]
