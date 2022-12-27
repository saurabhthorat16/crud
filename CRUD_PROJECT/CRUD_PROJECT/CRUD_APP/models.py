from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    addr = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.sid}-{self.fname}-{self.lname}-{self.addr}-{self.email}'

class Fees(models.Model):
    stid = models.OneToOneField(Student,on_delete=models.CASCADE)
    admino = models.IntegerField()
    fees = models.IntegerField()

    def __str__(self):
        return f'{self.stid}-{self.admino}-{self.fees}'