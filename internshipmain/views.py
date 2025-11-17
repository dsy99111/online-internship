from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm
from .models import Course, Testimonial, Instructor

def home(request):
    return render(request, 'internshipmain/index.html')

def about(request):
    instructor = Instructor.objects.first()
    return render(request, 'internshipmain/about.html', {'instructor': instructor})

def team(request):
    instructor = Instructor.objects.first()
    return render(request, 'internshipmain/team.html', {'instructor': instructor})

def courses(request):
    q = request.GET.get("q")

    if q:
        all_courses = Course.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(category__icontains=q) |
            Q(language__icontains=q)
        )
    else:
        all_courses = Course.objects.all()

    return render(request, "internshipmain/course.html", {
        "courses": all_courses,
        "query": q,
    })


# ❌ DELETE your old detail() view
# Only use this one:
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    related_courses = Course.objects.filter(category=course.category).exclude(id=id)[:3]

    return render(request, "internshipmain/detail.html", {
        "course": course,
        "related_courses": related_courses,
    })


def feature(request):
    return render(request, 'internshipmain/feature.html')

def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'internshipmain/testimonial.html', {'testimonials': testimonials})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'internshipmain/contact.html', {'form': form})
