# Generated by Django 2.2.10 on 2020-10-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platForm', '0003_auto_20201015_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='category_name',
            field=models.IntegerField(choices=[(1, 'rock'), (2, 'hophop'), (3, 'vacaloid')], default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='foo',
            field=models.IntegerField(choices=[(1, 'foo1'), (2, 'foo2'), (3, 'foo3')], default='SOME STRING'),
        ),
    ]
