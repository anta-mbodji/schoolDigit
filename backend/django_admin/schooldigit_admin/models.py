from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.name}"