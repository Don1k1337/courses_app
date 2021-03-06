# Generated by Django 2.2.2 on 2019-06-28 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='imgpath',
            field=models.CharField(default='', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses_app.Course'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses_app.Course'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_app.ContactValue'),
        ),
    ]
