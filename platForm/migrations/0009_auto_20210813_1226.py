# Generated by Django 2.2.10 on 2021-08-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platForm', '0008_auto_20201203_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='author',
            field=models.CharField(default=999, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contents',
            name='author_comment',
            field=models.CharField(default=122, max_length=100),
            preserve_default=False,
        ),
    ]
