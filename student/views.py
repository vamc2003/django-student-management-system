from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ContactForm

def home(request):
    return render(request, 'student/home.html')

def about(request):
    return render(request, 'student/about.html')

def contact(request):
    return render(request, 'student/contact.html')
def student_details(request):
    data = {
        'name': 'Vamshi',
        'age': 22,
        'course': 'Data Science'
    }

    return render(
        request,
        'student/details.html',
        data
    )

def student_list(request):
    students = Student.objects.all()

    search_query = request.GET.get('search')
    course_filter = request.GET.get('course')

    if search_query:
        students = students.filter(
            name__icontains=search_query
        ) | students.filter(
            email__icontains=search_query
        )

    if course_filter:
        students = students.filter(course=course_filter)

    courses = Student.objects.values_list(
        'course', flat=True
    ).distinct()

    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'student/student_list.html',
        {
            'students': page_obj,
            'courses': courses,
            'page_obj': page_obj,
            'search_query': search_query,
            'course_filter': course_filter,
        }
    )
    
def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'student/add_student.html',
        {'form': form}
    )

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'student/update_student.html',
        {'form': form}
    )
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()

        return redirect('student_list')

    return render(
        request,
        'student/delete_student.html',
        {'student': student}
    )
from .models import Student, School

def dashboard(request):

    total_students = Student.objects.count()

    total_schools = School.objects.count()

    total_courses = Student.objects.values(
        'course'
    ).distinct().count()

    recent_students = Student.objects.order_by(
        'id'
    )[:5]

    context = {
        'total_students': total_students,
        'total_schools': total_schools,
        'total_courses': total_courses,
        'recent_students': recent_students,
    }

    return render(
        request,
        'student/dashboard.html',
        context
    )
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(name, email, subject, message)

    else:
        form = ContactForm()

    return render(request, 'student/contact.html', {
        'form': form
    })