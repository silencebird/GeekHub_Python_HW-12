# Generated by Django 2.0.1 on 2018-02-02 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geekhub', '0004_auto_20180202_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geekhub.Course')),
            ],
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
        migrations.RemoveField(
            model_name='students',
            name='course_id',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]