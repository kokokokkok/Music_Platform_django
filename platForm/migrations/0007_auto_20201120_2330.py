# Generated by Django 2.2.10 on 2020-11-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platForm', '0006_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='contents',
            name='comment',
            field=models.CharField(default=999, max_length=100),
            preserve_default=False,
        ),
    ]
