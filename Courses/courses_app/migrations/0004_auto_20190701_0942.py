# Generated by Django 2.2.2 on 2019-07-01 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0003_auto_20190629_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses_app.Course'),
        ),
    ]
