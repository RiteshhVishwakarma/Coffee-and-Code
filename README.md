# Health-and-fitness-Tracker-
Hackverse project 

## 🧑‍💻 User Guide – FitTrack

Welcome to **FitTrack** – your personal fitness companion! This guide will help you get started with using the Wepapplication.

---

### 🚪 1. Getting Started

1. Visit the homepage of FitTrack.
2. Click on **Sign Up** to create a new account.
3. Already registered? Click **Login** to access your dashboard.

---

### 🏠 2. Dashboard Overview

Once logged in, you’ll be redirected to your **dashboard**, which includes:

- **Daily Fitness Logs** – Track workouts or physical activity.
- **Weekly Goals** – Set personalized fitness targets.
- **BMI & Calorie Calculator** – Calculate your ideal stats.
- **Profile** – View and edit your personal information.

---

### 📊 3. Using BMI & Calorie Calculator

1. Navigate to the **BMI Calculator** section.
2. Enter your height, weight, age, and activity level.
3. Click **Calculate** to view your BMI and suggested daily calorie intake.

---

### 📝 4. Editing Profile

1. Go to the **Profile Page** from the dashboard.
2. Click **Edit Profile** to update your:
   - Name
   - Age
   - Height / Weight
   - Profile Picture (optional)
3. Save changes to update your info.

---

### 🔒 5. Logging Out

- Click on the **Logout** button from the navbar or dashboard to end your session securely.

---

### 📌 Notes

- Ensure you are logged in to access your dashboard and log entries.
- All data is stored securely and is unique to your account.
- For the best experience, use on desktop or mobile browser in landscape mode.

---

Want me to help you write the rest of your README (like Installation, Features, Tech Stack)? Just say the word 😊


### 🏋️‍♂️ **FitTrack – Site Flow Structure**

```
Homepage (Landing Page)
   │
   ├──> Signup / Login
   │       └── Authenticated Session
   │               └── Redirect to Dashboard
   │
   ├──> Dashboard (Main User Area)
   │       ├── Daily Fitness Logs
   │       ├── Weekly Goals Tracking
   │       ├── BMI & Calorie Calculator
   │       └── Edit Profile (Update info, upload photo)
   │
   ├──> BMI & Calorie Page (if separate)
   │       └── Input: Height, Weight, Age, Activity
   │       └── Output: BMI Score + Daily Calorie Need
   │
   ├──> Profile Page
   │       └── Show Profile Info (Name, Age, Goals)
   │       └── Upload Profile Picture
   │       └── Edit Details Button
   │
   ├──> Logout
   │
   └──> Admin (Optional)
           └── Manage Users & Logs
```

---

### 🔄 **User Flow Summary**
1. **User Visits Homepage**
2. → Signs Up or Logs In  
3. → Enters Dashboard  
4. → Logs Daily Activity or Sets Weekly Goal  
5. → Calculates BMI & Calories  
6. → Edits Profile, Views Progress  
7. → Logs out securely

---

### 🔮 **Future Scope (Advanced Pages)**
- 📈 **Progress Graphs Page**
- 🗓️ **Calendar View of Logs**
- 💬 **Community / Tips Section**
- 📲 **Mobile App version (React Native)**