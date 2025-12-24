from django.contrib import admin
from trip.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_filter = ['email']
    list_display = ('name','email','created_date')
    search_fields = ('name','message')
    date_hierarchy = 'created_date'

    
    
admin.site.register(Contact,ContactAdmin)

