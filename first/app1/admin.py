from django.contrib import admin
from .models import Employee, License, Project, Task
# Register your models here.


admin.site.register([Employee, License, Task, Project])
















