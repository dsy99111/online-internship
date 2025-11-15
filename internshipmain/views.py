# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import Course, Testimonial, Instructor
def home(request):
    return render(request, 'internshipmain/index.html')

def about(request):
    return render(request, 'internshipmain/about.html')
def team(request):
    instructors = Instructor.objects.all()
    return render(request, 'internshipmain/team.html', {'instructors': instructors})


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'internshipmain/course.html', {'courses': all_courses})




def detail(request):
    return render(request, 'internshipmain/detail.html')
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)

    # Get related courses based on category (excluding current course)
    related_courses = Course.objects.filter(category=course.category).exclude(id=id)[:3]

    return render(request, "internshipmain/detail.html", {
        "course": course,
        "related_courses": related_courses,
    })
# ✅ Add these three
def feature(request):
    return render(request, 'internshipmain/feature.html')

def team(request):
    return render(request, 'internshipmain/team.html')

def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'internshipmain/testimonial.html', {'testimonials': testimonials})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'internshipmain/contact.html', {'form': form})

