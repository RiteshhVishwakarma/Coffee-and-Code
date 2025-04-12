from django.contrib import admin

# Register your models here.
# from .models import UserProfile, UserRole, UserStatus, UserType, UserPermission
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import UserProfile, DailyLog, WeeklyGoal

admin.site.register(UserProfile)
admin.site.register(DailyLog)
admin.site.register(WeeklyGoal)
# admin.site.register(MotivationalPrompt)