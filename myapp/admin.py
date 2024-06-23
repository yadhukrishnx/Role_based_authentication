from django.contrib import admin
from . models import LoginTable

# Register your models here

@admin.register(LoginTable)
class LoginAdmin(admin.ModelAdmin):
    list_display=('username','type')