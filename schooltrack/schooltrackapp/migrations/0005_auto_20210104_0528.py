# Generated by Django 3.1.4 on 2021-01-04 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooltrackapp', '0004_auto_20210104_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schooltrackapp.semester'),
            preserve_default=False,
        ),
    ]
