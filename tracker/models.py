from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Anonymous')
    age = models.IntegerField(default=18)  # Default age set to 18
    height = models.IntegerField(default=170)  # Default height in cm
    weight = models.FloatField(default=65.0)  # Default weight in kg
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')

    def __str__(self):
        return self.user.username


class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    calories_consumed = models.IntegerField(null=True, blank=True)  # in kcal
    calories_burned = models.IntegerField(null=True, blank=True)  # in kcal
    excersise_done = models.CharField(max_length=255, null=True, blank=True)  # e.g. "Running, Cycling"

    def __str__(self):
        return f'{self.user.username} Daily Log - {self.date}'


class WeeklyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start = models.DateField()
    water_goal = models.FloatField(help_text="Target water intake in liters")
    calorie_goal = models.IntegerField(help_text="Max calories per day")
    exercise_goal = models.CharField(max_length=255, help_text="Exercise targets for the week")

    def __str__(self):
        return f"{self.user.username} - Week of {self.week_start}"
