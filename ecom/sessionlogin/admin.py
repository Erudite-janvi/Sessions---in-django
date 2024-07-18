from django.contrib import admin

# Register your models here.
from .models import Session

class SessionAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    search_fields = ('username', 'password', 'email')

admin.site.register(Session,SessionAdmin)    
    