# Generated by Django 4.2.3 on 2023-07-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_desc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=25),
        ),
    ]
