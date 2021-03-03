# Generated by Django 3.1.6 on 2021-03-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscription', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_name',
        ),
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='course_thumbnails'),
        ),
    ]
