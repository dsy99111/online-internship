from django.shortcuts import render

def home(request):
    return render(request, 'internshipmain/index.html')

def about(request):
    return render(request, 'internshipmain/about.html')

def courses(request):
    return render(request, 'internshipmain/course.html')

def contact(request):
    return render(request, 'internshipmain/contact.html')

def detail(request):
    return render(request, 'internshipmain/detail.html')
# ✅ Add these three
def feature(request):
    return render(request, 'internshipmain/feature.html')

def team(request):
    return render(request, 'internshipmain/team.html')

def testimonial(request):
    return render(request, 'internshipmain/testimonial.html')


# Create your views here.
