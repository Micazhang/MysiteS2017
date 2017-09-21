# Register your models here.
from django.contrib import admin
from myapp.models import Author, Book, Course, Student, Topic
# Register your models here.



admin.site.register(Author)
admin.site.register(Topic)


class CourseAdmin (admin.ModelAdmin):
    filter_horizontal = ('students',)
admin.site.register(Course,CourseAdmin)


class BookAdmin(admin.ModelAdmin):
  list_display=['title','author','numpages','in_stock']
admin.site.register(Book, BookAdmin)

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','get_courses']
    # def register_courses(self,obj):
    #     register_courses = list(Student.objects.get(first_name=obj.firstname).course_set.all())
    #     return register_courses
# admin.site.register(Student,StudentAdmin)
admin.site.register(Student)