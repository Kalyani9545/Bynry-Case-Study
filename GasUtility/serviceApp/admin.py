from django.contrib import admin

# Register your models here.
from .models import Profile, Customer, Admin, Employees
from .models import Service, ServiceTicket

admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Employees)

admin.site.register(Service)
admin.site.register(ServiceTicket)
