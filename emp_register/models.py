from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.department

class Salary(models.Model):
    employee = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.employee
