from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid


class Users(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    Role_Choices = [('student', 'Student'),
                    ('instructor', 'Instructor'),
                    ('hod', 'HOD'),
                    ('tpo', 'TPO'),
                    ('admin', 'Admin')]
    username = models.CharField(max_length=150, unique=False, null=False, blank=False)
    email = models.EmailField(max_length=150, unique=True,blank=False)
    role  = models.CharField(max_length=25,null=False, blank=False, choices=Role_Choices)
    phone_no = models.PositiveIntegerField(null=True, blank= True)
    user_created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'username']
    
    def __str__(self):
        return f"{self.username} is {self.role}"

class Instructor(models.Model):
    instructor = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='instructor_profile')
    ins_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instructor.username}"


class Classes(models.Model):
    phase_choices = [('1', 'one'),
                        ('2', 'two'),
                        ('3', 'three')]
    class_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    phase = models.CharField(max_length= 50, null=False, blank=False, choices=phase_choices) #add choice ---> Done
    class_name = models.CharField(max_length=100)
    date = models.DateField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField(null = True)
    venue = models.CharField(max_length=150)
    total_students = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=False, related_name='classes')
    batch_id = models.IntegerField(null = False)
    batch_name = models.CharField(max_length= 10, null=False)
    class_created_at = models.DateTimeField(auto_now_add=True)

    def check_time(self):
        if self.end_time < self.start_time:
            raise ValidationError("End time must be after start time")

# -- Tell the overall roadmap of CRT,
#       DAT-1, orientation, phase1, Dat-2, etc.
# add class id
# boolean for all or particular
class Schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null = True)
    description = models.TextField(null = True, blank= True)

    def check_date(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date")

class TPO(models.Model):
    tpo = models.OneToOneField(Users, on_delete=models.CASCADE)
    branch_choices = [('CSE', 'CSE'),           
                        ('AIDS', 'AIDS'),       
                        ('MECH', 'MECH'),       
                        ('ELEC', 'ELEC'),       
                        ('CIVIL', 'CIVIL'),     
                        ('ECE', 'ECE'),         
                        ('IT', 'IT'),
                        ('CSAI', 'CSAI')]
    branch = models.CharField(max_length= 25, null=False, choices=branch_choices)
    tpo_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tpo.username} of {self.branch}"

class Student(models.Model):
    branch_choices = [('CSE', 'CSE'),
                        ('AIDS', 'AIDS'),
                        ('MECH', 'MECH'),
                        ('ELEC', 'ELEC'),
                        ('CIVIL', 'CIVIL'),
                        ('ECE', 'ECE'),
                        ('IT', 'IT'),
                        ('CSAI', 'CSAI')]

    phase_choices = [(1, 'one'),
                        (2, 'two'),
                        (3, 'three')]

    student = models.OneToOneField(Users, on_delete=models.CASCADE, related_name= 'Student_profile')
    rtu_roll_no = models.CharField(max_length=30, unique=True, null = False, blank= False)
    branch = models.CharField(max_length= 25, null=False, choices=branch_choices)
    batch_id = models.IntegerField(null=False)
    batch_name = models.CharField(max_length=10, null=False)
    attendance = models.PositiveIntegerField(default=0)
    score = models.IntegerField(default=0)
    tpo = models.ForeignKey(TPO, on_delete=models.DO_NOTHING)
    phase = models.IntegerField(null=False, choices=phase_choices)
    stu_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} having roll number {self.rtu_roll_no}"

class TechPerformance(models.Model):
    round_choices = [('R1', 'round1' ), ('R2', 'round2'), ('R3', 'round3'), ('R4', 'round4')]
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    interviewer = models.CharField(max_length=225, null = False, blank=False) #Name of the interviewer
    date = models.DateField(null = False)
    round = models.CharField(choices=round_choices, max_length=40, null=False, blank=False)
    remark = models.TextField(null = True, blank = True)
    score = models.PositiveIntegerField(null = False, blank=False)

class GD_ExtemporePerformance(models.Model):
    round_choices = [('R1', 'round1' ), ('R2', 'round2'), ('R3', 'round3'), ('R4', 'round4')]
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    interviewer = models.CharField(max_length=225, null = False, blank=False) #Name of the interviewer
    date = models.DateField(null = False)
    round = models.CharField(choices=round_choices, max_length=40, null=False, blank=False)
    remark = models.TextField(null = True, blank = True)
    score = models.PositiveIntegerField(null = False, blank=False)

class HRPerformance(models.Model):
    round_choices = [('R1', 'round1' ), ('R2', 'round2'), ('R3', 'round3'), ('R4', 'round4')]
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    interviewer = models.CharField(max_length=225, null = False, blank=False) #Name of the interviewer
    date = models.DateField(null = False)
    round = models.CharField(choices=round_choices, max_length=40, null=False, blank=False)
    remark = models.TextField(null = True, blank = True)
    score = models.PositiveIntegerField(null = False, blank=False)
    
    
class StudentConfig(models.Model):
    name = models.CharField(max_length=400)
    branch = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=60, unique=True)
    admin = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)
    password = models.CharField(max_length=128, default='defaultpassword')  # Temporary default

    def __str__(self):
        return f"{self.name} - {self.roll_number}"











