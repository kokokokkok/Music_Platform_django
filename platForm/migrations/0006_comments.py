# Generated by Django 2.2.10 on 2020-11-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platForm', '0005_remove_contents_foo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
    ]
