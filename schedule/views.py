from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm, ScheduleForm, StudentForm, TPOForm, InstructorForm, ClassForm
from .models import Users, Instructor, Student, Classes, Schedule, TPO
# from django.contrib.auth.hashers import make_password

# from .forms import ShowTimetable
# Create your views here.
# takes request and gives a response
# it is a request handler

# log errors --> remove try --->>> Done
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        phone_no = request.POST.get('phone_no')
        # password = make_password(request.POST.get('password'))  #hashed password
        user_created_at = request.POST.get('user_created_at')

        if not all([name, role, email]):
            return JsonResponse({'message' : 'Provide required fields'}, status=400)

        try:
            user = Users.objects.create(name = name, role = role, email = email, phone_no = phone_no, user_created_at = user_created_at)
            return JsonResponse({'message' : "User created succcessfully"}, status= 201)

        except Exception as e:
            return JsonResponse({'message' : str(e)}, status=500)
    
    return JsonResponse({'message' : 'Invalid request method'}, status=405)

@csrf_exempt
def create_instructor(request):
    if request.method == "POST":
        try:
            users = Users.objects.filter(role = 'instructor')
            ins_created_at = request.POST.get('ins_created_at')
            data = []

            for instructor_user in users:
                if not Instructor.objects.filter(instructor = instructor_user).exists():
                    instructor = Instructor.objects.create(instructor = instructor_user, ins_created_at = ins_created_at)
                    data.append({'name' :instructor.instructor.name, 
                                'email' :instructor.instructor.email,
                                'role' :instructor.instructor.role,
                                'phone_no' :instructor.instructor.phone_no,
                                'ins_created_at' : instructor.ins_created_at})   
            return JsonResponse({'data' : data}, safe=False)

        except Exception as e:
            return JsonResponse({'message' : str(e)}, status=500)
    return JsonResponse({'message' : 'Invlaid request method'}, status=405)   

@csrf_exempt
def create_TPO(request):
    if request.method == 'POST':
        try:
            branch = request.POST.get('branch')
            tpo_created_at = request.POST.get('tpo_created_at')
            data = []

            users = Users.objects.filter(role = 'TPO') 

            for tpo_user in users:
                if not TPO.objects.filter(tpo = tpo_user).exists():
                    tpo = TPO.objects.create(tpo = tpo_user,
                                                branch = branch,
                                                tpo_created_at = tpo_created_at)
                
                    data.append({'name' : tpo.tpo.name, 
                                'email' : tpo.tpo.email,
                                'role' : tpo.tpo.role,
                                'phone_no' : tpo.tpo.phone_no,
                                'branch' : tpo.branch,
                                'tpo_created_at' : tpo.tpo_created_at,
                                })
                    return JsonResponse({'data' : data})
        
        except Exception as e:
            return JsonResponse({'message' : str(e)}, status=500)
        
    return JsonResponse({'message' : 'Invalid request method'}, status=405)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            rtu_roll_no = request.POST.get('rtu_roll_no')
            batch_name = request.POST.get('batch_name')
            batch_id = request.POST.get('batch_id')
            attendance = request.POST.get('attendance') 
            score = request.POST.get('score')
            branch = request.POST.get('branch')
            phase = request.POST.get('phase')
            tpo = request.POST.get('tpo')
            stu_created_at = request.POST.get('stu_created_at')
            data = []

            users = Users.objects.filter(role = 'student')

            for student_user in users:
                if not Student.objects.filter(student = student_user).exists():
                    student = Student.objects.create(student = student_user,
                                                        rtu_roll_no=rtu_roll_no,
                                                        phase = phase,
                                                        batch_name=batch_name,
                                                        batch_id=batch_id,
                                                        attendance=attendance,
                                                        score=score,
                                                        tpo = tpo,
                                                        branch = branch,
                                                        stu_created_at = stu_created_at)
                    data.append({'name' : student.student.name, 
                                'rtu_roll_no' : student.student.rtu_roll_no,
                                'email' : student.student.email,
                                'role' : student.student.role,
                                'phone_no' : student.student.phone_no,
                                'branch' : student.branch,
                                'score' : student.score,
                                'batch_name' : student.batch_name,
                                'batch_id' : student.batch_id,
                                'attendance' : student.attendance,
                                'tpo' : student.tpo,
                                'stu_created_at' : student.stu_created_at,
                                'phase' : student.phase})
            return JsonResponse({'data' : data})
        
        except Exception as e:
            return JsonResponse({'message' : str(e)}, status=500)
        
    return JsonResponse({'message' : 'Invalid request method'}, status=405)

@csrf_exempt
def create_schedule(request):
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            name = request.POST.get('name')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            description = request.POST.get('description')

            if not all([id, name, start_date]):
                return JsonResponse({'error' : 'Provide required fields'})

            schedule = Schedule.objects.create(id = id,
                                                name = name,
                                                start_date = start_date,
                                                end_date = end_date,
                                                start_time = start_time,
                                                end_time = end_time,
                                                description = description)
                    
            return JsonResponse({'message' : 'Event created successully', 'class_id' : str(schedule.id)}, status=201)

        except Exception as e:
            return JsonResponse({'message' : str(e)}, status = 500)
    
    return JsonResponse({'message' : 'Invalid request method'}, status=405)

@csrf_exempt
def create_classes(request):
    if request.method == "POST":
        try:
            class_id = request.POST.get('class_id')
            class_name = request.POST.get('class_name')
            phase = request.POST.get('phase')
            date = request.POST.get('date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            venue = request.POST.get('venue')
            batch_name = request.POST.get('batch_name')
            instructor_id = request.POST.get('teacher_id')
            batch_id = request.POST.get('batch_id')
            total_students = request.POST.get('total_students')
            class_created_at = request.POST.get('class_created_at')

            if not all([instructor_id, batch_id]):
                return JsonResponse({'error' : 'Provide required fields'})

            Class = Classes.objects.create(class_id = class_id,
                                    class_name = class_name,
                                    phase = phase,
                                    date = date,
                                    start_time = start_time,
                                    end_time = end_time,
                                    venue = venue,
                                    batch_name = batch_name,
                                    instructor_id = instructor_id, 
                                    batch_id = batch_id,
                                    total_students = total_students,
                                    class_created_at = class_created_at)
        
            return JsonResponse({'message' : 'Class created successully', 'class_id' : str(Class.class_id)}, status=201)

        except Exception as e:
            return JsonResponse({'message' : str(e)}, status = 500)
    
    return JsonResponse({'message' : 'Invalid request method'}, status=405)


def view_class_timetable(request, class_id):
    clas = get_object_or_404(Classes, class_id = class_id)
    return render(request, r"C:\winter_proj\templates\class_timetable.html", {'class' : clas})


def user_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    
    return render(request, "user_form.html", {'form' : form})

def instructor_view(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InstructorForm()

    return render(request, "instructor_form.html", {'form' : form})

def tpo_view(request):
    if request.method == "POST":
        form = TPOForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TPOForm()
    
    return render(request, "tpo_form.html", {'form' : form})

def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = StudentForm()
    
    return render(request, "student_form.html", {'form' : form})

def schedule_view(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = ScheduleForm()
    return render(request, "schedule_form.html", {'form' : form})

def class_view(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = ClassForm()
    
    return render(request, r"C:\winter_proj\templates\class_from.html", {'form' : form})