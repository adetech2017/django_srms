# Generated by Django 4.0.3 on 2022-09-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0007_student_subject_result_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_subject_result',
            old_name='grade',
            new_name='total_score',
        ),
        migrations.AddField(
            model_name='result',
            name='session',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
