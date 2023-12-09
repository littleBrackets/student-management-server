from django.contrib import admin

# Register your models here.
from .models import School, SignUP

class signupAdmin(admin.ModelAdmin):
    list_display = ('idx', 'username', 'password')

class schoolAdmin(admin.ModelAdmin):
    list_display = ('idx', 'name', 'email', 'address', 'contact')

admin.site.register(SignUP, signupAdmin)
admin.site.register(School, schoolAdmin)