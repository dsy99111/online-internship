from django.contrib import admin
from .models import ContactMessage
from .models import Course, Testimonial, Instructor, SiteAbout

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'created_at')
    search_fields = ('name', 'email', 'mobile', 'subject')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'rating', 'language', 'price', 'category')
    search_fields = ('title', 'instructor', 'category')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'created_at')
    search_fields = ('name', 'course')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'image')
    search_fields = ('name', 'role')

@admin.register(SiteAbout)
class SiteAboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'section_title')
