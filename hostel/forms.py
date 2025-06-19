from django import forms
from .models import Student, Employee, Warden, Room, MessDetails, Complaint
from .models import Attendance

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'room', 'email', 'username', 'password']

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['name', 'position', 'email', 'username', 'password']

class WardenForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Warden
        fields = ['name', 'phone_number', 'email', 'username', 'password']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'capacity', 'current_students']


class MessDetailsForm(forms.ModelForm):
    class Meta:
        model = MessDetails
        fields = ['breakfast', 'lunch', 'snacks', 'dinner']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'description']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [] 
      
