# Generated by Django 4.0.4 on 2022-05-03 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='institute_id',
            new_name='institute',
        ),
    ]
