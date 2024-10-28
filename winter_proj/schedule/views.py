from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Instructor, Student, Classes

# Create your views here.
# takes request and gives a response
# it is a request handler

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        phone_no = request.POST.get('phone_no')
        branch = request.POST.get('branch')

        if not all([name, role, email]):
            return JsonResponse({'message' : 'Provide required fields'})
        
        user = Users.objects.create(name = name, role = role, email = email, phone_no = phone_no, branch = branch)
        return JsonResponse({'message' : "Instructor created succcessfully"})
    
@csrf_exempt
def create_instructor(request):
    if request.method == "POST":
        try:
            users = Users.objects.filter(role = 'instructor')
            data = []
            for instructor_user in users:
                if not Instructor.objects.filter(instructor = instructor_user).exists():
                    instructor = Instructor.objects.create(instructor = instructor_user)
                    data.append({'name' : instructor.instructor.name, 
                                'email' : instructor.instructor.email,
                                'role' : instructor.instructor.role,
                                'phone_no' : instructor.instructor.phone_no,
                                'branch' : instructor.instructor.branch})
                    
            return JsonResponse({'data' : data}, safe=False)
        
        except:
            pass

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            rtu_roll_no = request.POST.get('rtu_roll_no')
            users = Users.objects.filter(role = Student)
            data = []
            for student_user in users:
                if not Student.objects.filter(student = student_user).exists():
                    student = Student.objects.create(student = student_user)
                    data.append({'name' : student.student.name, 
                                'rtu_roll_no' : rtu_roll_no,
                                'email' : student.student.email,
                                'role' : student.student.role,
                                'phone_no' : student.student.phone_no,
                                'branch' : student.student.branch})
            return JsonResponse({'data' : data})
        
        except:
            pass

def create_classes(request):
    if request.method == "POST":
        class_name = request.POST.get('class_name')
        date = request.POST.get('date')
        start = request.POST.get('start_time')
        end = request.POST.get('end_time')
        instructor_id = request.POST.get('teacher_id')
        batch_id = request.POST.get('batch_id')

        if not all([instructor_id, date, start, batch_id]):
            return JsonResponse({'error' : 'Provide required fields'})
        
        Class = Classes.objects.create(class_name = class_name, date = date,
                                    start_time = start, end_time = end, instructor_id = instructor_id, 
                                    batch_id = batch_id)
        
        return JsonResponse({'message' : 'Class created successully'})

def get_instructor_timetable(request, instructr_id):
    timetable = Classes.objects.filter(instructor_id = instructr_id)
    data = []
    for t in timetable:
        data = [{'class_name' : t.class_name,
                'date' : t.date,
                'start_time' : t.start_time,
                'end_time' : t.end_time,
                'instructor_id' : t.instructor_id,
                'batch_id' : t.batch_id}]

    return JsonResponse(data, safe= False)

def get_student_timetable(request, student_id):
    student = Student.objects.filter(student_id = student_id)
    btch_id = student.batch_id
    timetable = Classes.objects.filter(batch_id = btch_id)
    data = []
    for t in timetable:
        data = [{'class_name' : t.class_name,
                'date' : t.date,
                'start_time' : t.start_time,
                'end_time' : t.end_time,
                'instructor_id' : t.instructor_id,
                'batch_id' : t.batch_id}]
    
    return JsonResponse(data, safe= False)


# @csrf_exempt
# def create_Teacher(request):
#     try:
#         if request.method == "POST":
#             name = request.POST.get('Teacher_name')
#             email = request.POST.get('Teacher_email')
#             batch_id = request.POST.get('Batch_assigned_id')

#             if not all([name, email, batch_id]):
#                 return HttpResponse("All fields are required")
            
#             teacher = Teacher.objects.create(Teacher_name = name, Teacher_email = email, Batch_assigned_id = batch_id)
#             return HttpResponse("Teacher created successfully, {}".format(teacher.id))
            
#     except:
#         pass

# @csrf_exempt
# def create_Student(requset):
#     try:
#         if requset.method == "POST":
#             name = requset.POST.get('Student_name')
#             dept = requset.POST.get('Student_dept')
#             email = requset.POST.get('Student_email')
#             batch_id = requset.POST.get('Student_batch_id')

#             if not all([name, email, batch_id]):
#                 return HttpResponse("Fill the required fields")
            
#             student = Students.objects.create(Student_name = name, Student_dept = dept, Student_email = email, Student_batch_id = batch_id)
#             return HttpResponse("Student successfully created, {}".format(student.id))
    
#     except:
#         pass

# @csrf_exempt
# def create_schedule(request):
#     if request.method == "POST":
#         subject = request.POST.get('Subject')
#         start_time = request.POST.get('Start_Time')
#         end_time = request.POST.get('End_Time')
#         date = request.POST.get('Date')
#         batch_id = request.POST.get('Batch_id')
    # if not all([subject, start_time, end_time, date, batch_id]) :
    #     return HttpResponse("All fields are required")
    # schedule = Schedule.objects.create(Subject = subject, Start_Time = start_time, End_Time = end_time, Date = date, B)