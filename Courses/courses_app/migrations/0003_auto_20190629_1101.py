# Generated by Django 2.2.2 on 2019-06-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_auto_20190628_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='imgpath',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('PHONE', 'PHONE'), ('FACEBOOK', 'FACEBOOK'), ('EMAIL', 'EMAIL')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.DeleteModel(
            name='ContactValue',
        ),
    ]
