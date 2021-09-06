from django.contrib import admin
from .models import Contact,Friendspost
# Register your models here.

#admin.site.register(Contact)
admin.site.register(Friendspost)

#admin.site.register(Adminpost)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'desc')

    search_fields = ('name','phone')
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)