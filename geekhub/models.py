from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateTimeField(help_text='date of the courses beginning ')
    descriptions = models.TextField(max_length=300, blank=True)
    requirements = ArrayField(models.CharField(max_length=100, blank=True), blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)


class New(models.Model):
    date = models.DateTimeField(help_text='publish date')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    source_url = models.URLField(blank=True)

    def __str__(self):
        return "{} {}".format(self.date, self.title)
