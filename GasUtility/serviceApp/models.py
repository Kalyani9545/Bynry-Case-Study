from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)

    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default=None)

    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)

    def __str__(self):
        return self.user.name

class Admin(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)

    def __str__(self):
        return self.user.name
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    service_charge = models.IntegerField(default=0)

    created_by = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    
    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)

    def __str__(self):
        return self.name
    
class Employees(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)

    def __str__(self):
        return self.user.name
    
class ServiceTicket(models.Model):
    class Status(models.TextChoices):
        CRET = "1", "CREATED"
        SEEN = "2", "SEEN"
        INPR = "3", "INPROCESS"
        RESD = "4", "RESOLVED"
        
    ticket = models.ForeignKey(Service, on_delete=models.DO_NOTHING)    
    description = models.CharField(max_length=256)
    attachment = models.FileField(upload_to='tickets/')
    status = models.CharField(max_length=4, choices=Status.choices,default=Status.CRET)
    created_by = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    
    created_at = models.DateTimeField("created date", auto_now_add=True)
    updated_at = models.DateTimeField("update date", auto_now=True)

    def __str__(self):
        return self.ticket.name