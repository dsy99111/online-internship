from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/", blank=True, null=True)

    instructor = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    reviews_count = models.IntegerField(default=0)
    language = models.CharField(max_length=50, default="English")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    category = models.CharField(max_length=100, default="General")  # For related courses

    def __str__(self):
        return self.title
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to="instructors/", blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
