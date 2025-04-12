# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import DailyLog

class CustomUserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    height = forms.IntegerField()
    weight = forms.FloatField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                age=self.cleaned_data['age'],
                height=self.cleaned_data['height'],
                weight=self.cleaned_data['weight'],
                gender=self.cleaned_data['gender']
            )
        return user

# New Login Form
class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)



from django import forms
from .models import DailyLog

class WaterIntakeForm(forms.ModelForm):
    water_intake = forms.FloatField(
        label='Water Intake (litres)',
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={'step': 0.1})
    )

    class Meta:
        model = DailyLog
        fields = ['water_intake']

class CalorieForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['calories']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['exercise_duration']