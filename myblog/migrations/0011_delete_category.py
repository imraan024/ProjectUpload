# Generated by Django 3.2.6 on 2021-08-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_alter_post_post_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
