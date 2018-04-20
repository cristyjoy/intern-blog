# Generated by Django 2.0.4 on 2018-04-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0006_auto_20180420_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('hidden', 'Hidden')], default='draft', max_length=10),
        ),
    ]