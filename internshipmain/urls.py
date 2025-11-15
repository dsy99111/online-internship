from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),   # ✅ Add this line
    path('feature/', views.feature, name='feature'),       # ✅ Added
    path('team/', views.team, name='team'),               # ✅ Added
    path('testimonial/', views.testimonial, name='testimonial'),  # ✅ Added
    path('course/<int:id>/', views.course_detail, name='course_detail'),

]
