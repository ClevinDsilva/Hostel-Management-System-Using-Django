from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} ({self.roll_number})'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Warden(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Room(models.Model):
    room_number = models.CharField(max_length=5, unique=True)
    capacity = models.IntegerField(default=4)
    current_students = models.ManyToManyField(Student, blank=True, related_name="roommates")

    def __str__(self):
        return self.room_number

class MessDetails(models.Model):
    day = models.CharField(max_length=10, default='Monday')  
    breakfast = models.CharField(max_length=255, default='')  
    lunch = models.CharField(max_length=255, default='')      
    snacks = models.CharField(max_length=255, default='')     
    dinner = models.CharField(max_length=255, default='')     

    def __str__(self):
        return f"{self.day} - {self.breakfast}, {self.lunch}, {self.snacks}, {self.dinner}"


    
class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)  # This acts as the title
    description = models.TextField()

    def __str__(self):
        return f'Complaint by {self.student.name} - {self.subject}'

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    class Meta:
        unique_together = ('student', 'date')  # Ensure one record per day

    def __str__(self):
        return f"Attendance for {self.student.name} on {self.date} at {self.time}"