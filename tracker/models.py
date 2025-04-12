from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# UserProfile model to store additional information about the user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    # location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True) # in cm
    weight = models.FloatField(null=True, blank=True) # in kg

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # Daily Log model to store daily logs of the user
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # weight = models.FloatField(null=True, blank=True) # in kg
    calories_consumed = models.IntegerField(null=True, blank=True) # in kcal
    calories_burned = models.IntegerField(null=True, blank=True) # in kcal
    excersise_done = models.CharField(max_length=255, null=True, blank=True) # e.g. "Running, Cycling"
    # steps_walked = models.IntegerField(null=True, blank=True) # in steps

    def __str__(self):
        return f'{self.user.username} Daily Log - {self.date}'
    

#  Weekly goal model to store weekly goals of the user
class WeeklyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start = models.DateField()
    water_goal = models.FloatField(help_text="Target water intake in liters")
    calorie_goal = models.IntegerField(help_text="Max calories per day")
    exercise_goal = models.CharField(max_length=255, help_text="Exercise targets for the week")

    def __str__(self):
        return f"{self.user.username} - Week of {self.week_start}"


# Otptional model to store motivational prompts for the user

# class MotivationalPrompt(models.Model):
#     text = models.CharField(max_length=255)

#     def __str__(self):
#         return self.text
