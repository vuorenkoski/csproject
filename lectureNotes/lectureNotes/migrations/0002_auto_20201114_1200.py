# Generated by Django 3.1.3 on 2020-11-14 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lectureNotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectureNotes.course'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectureNotes.note'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
