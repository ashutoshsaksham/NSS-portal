# Generated by Django 4.0.4 on 2022-05-20 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_student_email_alter_student_full_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
