from django.contrib import admin
from .models import Jobs,Status,Job_type,Dept


class jobs_admin(admin.ModelAdmin):
   
    list_display = ('title', 'start_date','updated_date')
 
admin.site.register(Jobs,jobs_admin)
admin.site.register(Status)
admin.site.register(Job_type)
admin.site.register(Dept)
