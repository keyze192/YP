from django.contrib import admin
from .models import Request, Service, MyUser

admin.site.register(Request)
admin.site.register(Service)
admin.site.register(MyUser)