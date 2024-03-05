from django.db import models

# Create your models here.

class Dept(models.Model):
    deptid = models.IntegerField(primary_key = True)
    dname = models.CharField(max_length = 10)
    dloc = models.CharField(max_length = 10)
    def __str__(self):
        return self.dname
class Emp(models.Model):
    empid = models.IntegerField(primary_key = True)
    deptid = models.ForeignKey(Dept,on_delete = models.CASCADE)
    ename = models.CharField(max_length = 10)
    esal = models.IntegerField() 
    def __str__(self):
        return self.ename