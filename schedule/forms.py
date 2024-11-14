from django import forms
from .models import Users, Classes,  Instructor, Student, Schedule, TPO

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'role', 'phone_no']
        widgets = {'name' : forms.TextInput(attrs={'placeholder' : 'Name'}),
                    'email' : forms.EmailInput(attrs={'placeholder' : 'Enter your email'}),
                    'role' : forms.Select(choices=[('student', 'Student'),('instructor', 'Instructor'),('hod', 'HOD'),('tpo', 'TPO')]),
                    'phone_no' : forms.TextInput(attrs={'placeholder': 'Phone number'})}

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor']
        widgets = {'instructor' : forms.Select(attrs={'placeholder' : 'Instructor'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = Users.objects.filter(role='instructor')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student', 'rtu_roll_no', 'branch', 'batch_name', 'batch_id', 'attendance', 'score', 'tpo', 'phase']
        widgets = {'student' : forms.Select(attrs={'placeholder' : 'Student'}),
                    'rtu_roll_no' : forms.TextInput(attrs={'placeholder' : 'RTU_roll_no'}),
                    'branch' :forms.Select(choices=[('CSE', 'CSE'), ('AIDS', 'AIDS'), ('MECH', 'MECH'), ('ELEC', 'ELEC'),       
                                                    ('CIVIL', 'CIVIL'), ('ECE', 'ECE'), ('IT', 'IT'), ('CSAI', 'CSAI')]),
                    'batch_name' : forms.TextInput(attrs={'placeholder' : 'Batch name'}),
                    'batch_id' : forms.TextInput(attrs={'placeholder' : 'Batch id'}),
                    'attendance' : forms.NumberInput(attrs={'placeholder' : 'Attendance'}),
                    'score' : forms.NumberInput(attrs={'placeholder' : 'Score'}),
                    'tpo' : forms.Select(attrs={'placeholder' : 'TPO'}),
                    'phase' : forms.Select(choices=[(1, 'one'),
                                                    (2, 'two'),
                                                    (3, 'three')])}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Users.objects.filter(role='student')
        self.fields['tpo'].queryset = TPO.objects.all()

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['name', 'start_date', 'end_date', 'start_time', 'end_time', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.TextInput(attrs={'placeholder': 'Event Description'})}

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['class_name', 'phase', 'date', 'start_time', 'end_time', 'venue', 'batch_name', 'instructor', 'batch_id', 'total_students']
        widgets = {'class_name': forms.TextInput(attrs={'placeholder': 'Class Name'}),
                    'phase': forms.Select(choices=[(1, 'one'),
                                            (2, 'two'),
                                            (3, 'three')]),
                    'date': forms.DateInput(attrs={'type': 'date'}),
                    'start_time': forms.TimeInput(attrs={'type': 'time'}),
                    'end_time': forms.TimeInput(attrs={'type': 'time'}),
                    'venue': forms.TextInput(attrs={'placeholder': 'Venue'}),
                    'batch_name': forms.TextInput(attrs={'placeholder': 'Batch Name'}),
                    'instructor': forms.Select(attrs={'placeholder' : 'Instructor'}),
                    'batch_id' : forms.NumberInput(attrs={'placeholder' : 'Batch ID'}),
                    'total_students' : forms.NumberInput(attrs={'placeholder' : 'Total no. of students'})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructor'].queryset = Instructor.objects.all()


class TPOForm(forms.ModelForm):
    class Meta:
        model = TPO
        fields = ['tpo', 'branch']
        widgets = {'tpo' : forms.Select(attrs={'placeholder' : 'TPO'}),
                    'branch' :forms.Select(choices=[('CSE', 'CSE'), ('AIDS', 'AIDS'), ('MECH', 'MECH'), ('ELEC', 'ELEC'),       
                                                    ('CIVIL', 'CIVIL'), ('ECE', 'ECE'), ('IT', 'IT'), ('CSAI', 'CSAI')])}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tpo'].queryset = Users.objects.filter(role='tpo')
