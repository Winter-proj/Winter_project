from django.db import models
import uuid

# Create your models here.
# class Teacher(models.Model):
#     Teacher_name = models.CharField(max_length= 100)
#     Teacher_email = models.CharField(max_length=100)
#     Batch_assigned_id = models.IntegerField()
# class Students(models.Model):
#     Student_name = models.CharField(max_length = 100)
#     Student_dept = models.CharField(max_length = 20)
#     Student_email = models.CharField(max_length=  100)
#     Student_batch_id = models.ImageField()

# class Schedule(models.Model):
#     Subject = models.CharField(max_length= 100)
#     Start_Time = models.TimeField()
#     End_Time = models.TimeField() 
#     Date = models.DateField()
#     Batch_id = models.IntegerField()
#     Teacher_id = models.IntegerField()

# branched ke namm save
#  user select kr ska hai
# foreign key se krna hai, nhi ho toh manytoone field

# class event, ins ki forign, classes ki foreign, time, date ---> admin pe create google ki api call and schedule event
#  google notes ka reminder bhi set ho jaye

class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    Role_Choices = [('student', 'Student'), ('instructor', 'Instructor'), ('hod', 'HOD'), ('tpo', 'TPO')]
    name = models.CharField(max_length= 100)
    role  = models.CharField(max_length=25,null=False, blank=False, choices=Role_Choices)
    email = models.EmailField(max_length= 150, null = False)
    phone_no = models.ImageField()
    branch = models.CharField(max_length=50, null = True)

class Instructor(models.Model):
    instructor = models.OneToOneField(Users, on_delete=models.CASCADE)

class Student(models.Model):
    student = models.OneToOneField(Users, on_delete=models.CASCADE)
    rtu_roll_no = models.CharField(max_length=30, null = False, blank= False)

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null = True)
    instructor_id = models.IntegerField(null=False)
    batch_id = models.IntegerField(null = False)

# class Branch(models.Model):
#     branch_name = models.CharField(null = False, unique=True)
#     students = models.CharField()

#     def set_students(self, student_list):
#         self.students = "_".join(student_list)

#     def get_students(self):
#         return self.students.split(", ")






