# Generated by Django 3.0.3 on 2020-03-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20200216_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='', max_length=120, upload_to='storage'),
            preserve_default=False,
        ),
    ]
