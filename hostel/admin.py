from django.contrib import admin
from .models import Student, Employee, Warden, Room, MessDetails, Complaint

admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Warden)
admin.site.register(Room)
admin.site.register(MessDetails)
admin.site.register(Complaint)
