# Generated by Django 3.1.6 on 2021-02-24 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_course_notes_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='course_id',
            new_name='courses_id',
        ),
    ]
