# Generated by Django 2.2.2 on 2019-07-03 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_auto_20190701_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses_app.Course'),
            preserve_default=False,
        ),
    ]