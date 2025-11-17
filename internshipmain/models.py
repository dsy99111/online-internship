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

class SiteAbout(models.Model):
    # Hero section
    heading = models.CharField(max_length=200, default="About Internship Online")
    subheading = models.CharField(
        max_length=300,
        default="Practical Learning • Real-World Projects • Career-Focused Internships"
    )

    # Main about content
    section_title = models.CharField(
        max_length=200,
        default="Empowering Students in Computer Science"
    )
    paragraph1 = models.TextField(blank=True, null=True)
    paragraph2 = models.TextField(blank=True, null=True)

    # About image
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    # Mission & vision
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_text = models.TextField(blank=True, null=True)
    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_text = models.TextField(blank=True, null=True)

    # Why choose us – 3 boxes
    box1_title = models.CharField(max_length=200, default="Hands-on Projects")
    box1_text = models.TextField(blank=True, null=True)

    box2_title = models.CharField(max_length=200, default="Learn from Expert Mentors")
    box2_text = models.TextField(blank=True, null=True)

    box3_title = models.CharField(max_length=200, default="Certificate & Portfolio")
    box3_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "About Page Content"
