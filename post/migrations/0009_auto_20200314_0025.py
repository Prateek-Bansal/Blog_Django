# Generated by Django 3.0.4 on 2020-03-13 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20200314_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category_name',
            new_name='category',
        ),
    ]
