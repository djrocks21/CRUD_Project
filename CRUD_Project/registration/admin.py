from django.contrib import admin
from .models import KeyUser
# Register your models here.


admin.site.register(KeyUser)

class KeyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password') 









