# Generated by Django 3.2.5 on 2021-07-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(default='6000000000'),
        ),
    ]
