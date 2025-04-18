# Generated by Django 5.1.7 on 2025-04-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_rename_exercise_done_dailylog_excersise_done_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailylog',
            old_name='calories_burned',
            new_name='calories',
        ),
        migrations.RenameField(
            model_name='dailylog',
            old_name='calories_consumed',
            new_name='exercise_duration',
        ),
        migrations.RemoveField(
            model_name='dailylog',
            name='excersise_done',
        ),
        migrations.RemoveField(
            model_name='weeklygoal',
            name='week_start',
        ),
        migrations.AlterField(
            model_name='weeklygoal',
            name='calorie_goal',
            field=models.IntegerField(default=14000),
        ),
        migrations.AlterField(
            model_name='weeklygoal',
            name='exercise_goal',
            field=models.IntegerField(default=210),
        ),
    ]
