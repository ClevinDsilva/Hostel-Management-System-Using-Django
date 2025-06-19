from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Employee, Warden, Room, MessDetails, Complaint
from .forms import StudentForm, EmployeeForm, WardenForm, RoomForm, MessDetailsForm, ComplaintForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import AttendanceForm
from .models import Attendance

def home(request):
    return render(request, 'hostel/base.html')

def custom_logout(request):
    user = request.user
    logout(request)
    
    if user.is_superuser:
        return redirect('admin_login')  
    elif hasattr(user, 'warden'):  
        return redirect('warden_login')  
    elif hasattr(user, 'student'):  
        return redirect('student_login')  
    else:
        return redirect('login')  
    
@login_required  
def mark_attendance(request):
    try:
        
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
    
        return render(request, 'hostel/attendance_error.html', {'message': 'You are not a registered student.'})

    today = timezone.now().date()

    
    if Attendance.objects.filter(student=student, date=today).exists():
        return render(request, 'hostel/attendance_error.html', {'message': 'You have already marked attendance for today.'})

    # If attendance doesn't exist, mark it
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = student  
            attendance.date = today  
            attendance.time = timezone.now()  
            attendance.save()
            return redirect('attendance_success')  
    else:
        form = AttendanceForm()

    return render(request, 'hostel/mark_attendance.html', {'form': form, 'student': student})

def view_attendance(request):
    attendance_records = Attendance.objects.all().order_by('-date', '-time')  
    return render(request, 'hostel/view_attendance.html', {'attendance_records': attendance_records})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:  # Check if the user is an admin
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to the admin dashboard
            else:
                messages.error(request, 'You are not authorized to access the admin dashboard.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'hostel/admin_login.html')

# Admin Dashboard
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    students = Student.objects.all()
    employees = Employee.objects.all()
    wardens = Warden.objects.all()
    rooms = Room.objects.all()
    mess_details = MessDetails.objects.all()
    return render(request, 'hostel/admin_dashboard.html', {
        'students': students,
        'employees': employees,
        'wardens': wardens,
        'rooms': rooms,
        'mess_details': mess_details
    })
    

@user_passes_test(is_admin)
def admin_dashboard(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render(request, 'hostel/admin_dashboard.html', {'days': days})

# Add Student
@user_passes_test(is_admin)
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            student = form.save(commit=False)
            student.user = user
            student.save()
            return redirect('admin_dashboard')
    else:
        form = StudentForm()
    return render(request, 'hostel/add_student.html', {'form': form})

# Update Student
@user_passes_test(is_admin)
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'hostel/update_student.html', {'form': form})

# Delete Student
@user_passes_test(is_admin)
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('admin_dashboard')

# Add Employee
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            employee = form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect('admin_dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'hostel/add_employee.html', {'form': form})

# Update Employee
@user_passes_test(is_admin)
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hostel/update_employee.html', {'form': form})

# Delete Employee
@user_passes_test(is_admin)
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('admin_dashboard')

def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'hostel/view_employees.html', {'employees': employees})

# Add Room
@user_passes_test(is_admin)
def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = RoomForm()
    return render(request, 'hostel/add_room.html', {'form': form})

# Update Room
@login_required
def update_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = RoomForm(instance=room)
    return render(request, 'hostel/update_room.html', {'form': form})

# Delete Room
@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    room.delete()
    return redirect('admin_dashboard')

def view_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'hostel/view_rooms.html', {'rooms': rooms})

# View Mess Details (accessible to all users, but only admins can edit or delete)

def view_mess_details(request):
    mess_details = MessDetails.objects.all()
    
    # Create a dictionary for easier access in the template
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    mess_details_by_day = {day: {'breakfast': 'N/A', 'lunch': 'N/A', 'snacks': 'N/A', 'dinner': 'N/A'} for day in days_of_week}
    
    for mess in mess_details:
        # Assume menu is a dictionary or JSON that contains the meal details
        menu = mess.menu
        for day in days_of_week:
            if day in menu:
                mess_details_by_day[day] = menu[day]
    
    return render(request, 'hostel/view_mess_details.html', {
        'mess_details_by_day': mess_details_by_day,
    })

# Add Mess Details (Admin Only)
@user_passes_test(is_admin)
def add_mess_details(request, day):
    if request.method == "POST":
        form = MessDetailsForm(request.POST)
        if form.is_valid():
            mess_detail = form.save(commit=False)
            mess_detail.day = day
            mess_detail.save()
            return redirect('view_mess_details')
    else:
        form = MessDetailsForm()
    return render(request, 'hostel/add_mess_details.html', {'form': form, 'day': day})

# Edit Mess Details (Admin Only)
@user_passes_test(is_admin)
def edit_mess_details(request, pk):
    mess_detail = get_object_or_404(MessDetails, pk=pk)
    if request.method == "POST":
        form = MessDetailsForm(request.POST, instance=mess_detail)
        if form.is_valid():
            form.save()
            return redirect('view_mess_details')
    else:
        form = MessDetailsForm(instance=mess_detail)
    return render(request, 'hostel/edit_mess_details.html', {'form': form})

# Delete Mess Details (Admin Only)
@user_passes_test(is_admin)
def delete_mess_details(request, pk):
    mess_detail = get_object_or_404(MessDetails, pk=pk)
    if request.method == "POST":
        mess_detail.delete()
        return redirect('view_mess_details')
    return render(request, 'hostel/delete_mess_details.html', {'mess_detail': mess_detail})

# Student Login
def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:  # Check if the user is active
                login(request, user)
                return redirect('student_dashboard')  # Redirect to the student dashboard
            else:
                messages.error(request, 'Your account is inactive.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'hostel/student_login.html')

# Student Dashboard
@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    mess_details = MessDetails.objects.all()  

    return render(request, 'hostel/student_dashboard.html', {
        'student': student,
        'mess_details': mess_details,
    })

# View Mess Details
@login_required
def view_mess_details(request):
    mess_details = MessDetails.objects.all()
    return render(request, 'hostel/view_mess_details.html', {
        'mess_details': mess_details,
    })

@login_required
def view_mess_items(request):
    mess_details = MessDetails.objects.all()
    return render(request, 'hostel/view_mess_items.html', {
        'mess_details': mess_details,
    })

@login_required
def view_roommates(request):
    student = get_object_or_404(Student, user=request.user)
    
    # Ensure the student has a room assigned
    if not student.room:
        messages.error(request, "You have not been assigned to a room.")
        return redirect('student_dashboard')

    # Get roommates by excluding the current student
    roommates = Student.objects.filter(room=student.room).exclude(id=student.id)

    return render(request, 'hostel/view_roommates.html', {
        'roommates': roommates,
    })


@login_required
def raise_complaint(request):
    student = get_object_or_404(Student, user=request.user)
    
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student = student  # Attach the current student to the complaint
            complaint.save()
            return redirect('student_dashboard')  # Redirect after successful submission
    else:
        form = ComplaintForm()
    
    return render(request, 'hostel/raise_complaint.html', {'form': form})

@login_required
def view_complaints(request):
    # Check if the user is a student or staff and filter complaints accordingly
    try:
        student = Student.objects.get(user=request.user)
        # Students see only their complaints
        complaints = Complaint.objects.filter(student=student)
    except Student.DoesNotExist:
        # Admins or wardens can see all complaints
        complaints = Complaint.objects.all()

    return render(request, 'hostel/view_complaints.html', {'complaints': complaints})

# Warden Login
def warden_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if the user is active
            if user.is_active:
                login(request, user)
                return redirect('warden_dashboard')  # Redirect to the Warden dashboard
            else:
                messages.error(request, 'Your account is inactive.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'hostel/warden_login.html')

@login_required
def warden_dashboard(request):
    students = Student.objects.all()
    employees = Employee.objects.all()
    rooms = Room.objects.all()
    mess_details = MessDetails.objects.all()
    return render(request, 'hostel/warden_dashboard.html', {
        'students': students,
        'employees': employees,
        'rooms': rooms,
        'mess_details': mess_details
    })

# Add Warden
@user_passes_test(is_admin)
def add_warden(request):
    if request.method == "POST":
        form = WardenForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            warden = form.save(commit=False)
            warden.user = user
            warden.save()
            return redirect('admin_dashboard')
    else:
        form = WardenForm()
    return render(request, 'hostel/add_warden.html', {'form': form})

# Update Warden
@user_passes_test(lambda user: user.is_staff)
def update_warden(request, warden_id):
    warden = get_object_or_404(Warden, pk=warden_id)
    if request.method == "POST":
        form = WardenForm(request.POST, instance=warden)
        if form.is_valid():
            form.save()
            return redirect('warden_dashboard')
    else:
        form = WardenForm(instance=warden)
    return render(request, 'hostel/update_warden.html', {'form': form})

# Delete Warden
@user_passes_test(lambda user: user.is_staff)
def delete_warden(request, warden_id):
    warden = get_object_or_404(Warden, pk=warden_id)
    warden.delete()
    return redirect('warden_dashboard')

# View Students
@login_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'hostel/view_students.html', {'students': students})

@login_required
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'hostel/view_employees.html', {'employees': employees})

# View Wardens
@user_passes_test(is_admin)
def view_wardens(request):
    wardens = Warden.objects.all()
    return render(request, 'hostel/view_wardens.html', {'wardens': wardens})