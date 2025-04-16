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

    @property
    def bmi(self):
        # Convert height to meters and calculate BMI
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return round(bmi, 1)

    @property
    def daily_calories(self):
        # Calculate BMR based on gender
        if self.gender == 'male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

        # For simplicity, assuming sedentary activity level (adjust if needed)
        calories = bmr * 1.2
        return round(calories)

    def __str__(self):
        return self.user.username


class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    water_intake = models.FloatField(null=True, blank=True)  # in litres
    calories = models.IntegerField(null=True, blank=True)    # in kcal
    exercise_duration = models.IntegerField(null=True, blank=True)  # in minutes

    def __str__(self):
        return f'{self.user.username} - {self.date}'


class WeeklyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    water_goal = models.FloatField(help_text="Target water intake in liters")
    calorie_goal = models.IntegerField(default=14000)
    exercise_goal = models.IntegerField(default=210)

    def __str__(self):
        return f"{self.user.username} - Weekly Goal"


class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    water_goal = models.FloatField(default=2.0)
    calories_goal = models.IntegerField(default=2000)
    exercise_goal = models.IntegerField(default=60)

    # def __str__(self):
    #     return f"{self.user.username} - Goal"