from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    city = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.lastname

def validate_numpages(value):
    if value < 50 or value > 1000:
        raise ValidationError('Numpages should between 50 and 1000')
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    in_stock = models.BooleanField(default=True)

    numpages = models.IntegerField(null=True, blank=True, validators=[validate_numpages])
    def __str__(self):
        return self.title

class Student(User):
    PROVINCE_CHOICES = (
        ('AB','Alberta'), # First value is stored in db, the second is descriptive
        ('MB','Manitoba'),
        ('ON','Ontario'),
        ('QC','Quebec'),
    )
    # firstname = models.CharField(max_length=50, null=True, blank=True)
    # lastname = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    age = models.IntegerField(null=True, blank=True)
  #  photo = models.ImageField(null=True, blank=True, upload_to='photos')
    def __str__(self):
        return self.last_name

class Course(models.Model):
    course_no = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    textbook = models.ForeignKey(Book, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    def __str__(self):
        return str(self.course_no)+' '+ self.title

    # def __iter__(self):
    #     return self.title

class Topic(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    intro_course = models.BooleanField(default=True)
    NO_PREFERENCE = 0
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afernoon'),
        (3, 'Evening')
    )
    time = models.IntegerField(default=0, choices=TIME_CHOICES)
    num_responses = models.IntegerField(default=0)
    avg_age = models.IntegerField(default=20)
    def __str__(self):
        return self.subject