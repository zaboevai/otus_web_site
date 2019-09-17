# Generated by Django 2.2.5 on 2019-09-17 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_school', '0003_auto_20190917_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student_id',
            new_name='student_fk',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher_fk',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='type',
            new_name='type_fk',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='course_id',
            new_name='course_fk',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='lesson_id',
            new_name='lesson_fk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='course_id',
        ),
        migrations.AddField(
            model_name='course',
            name='lesson_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='online_school.Lesson'),
        ),
        migrations.AddField(
            model_name='student',
            name='course_fk',
            field=models.ManyToManyField(blank=True, to='online_school.Course'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='course_fk',
            field=models.ManyToManyField(blank=True, to='online_school.Course'),
        ),
    ]
