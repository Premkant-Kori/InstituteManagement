from django.db import models


# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=30, null=False, blank=False)
    course_desc = models.TextField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.course_title
