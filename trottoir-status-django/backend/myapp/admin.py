from django.contrib import admin


from .models import Myapp

class MyappAdmin(admin.ModelAdmin):
    list_display = ("title","description","completed")


admin.site.register(Myapp,MyappAdmin)