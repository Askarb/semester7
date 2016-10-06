from django.contrib import admin
from book.models import Books, Customer


class BookAdmin(admin.ModelAdmin):
    list = ('name')
    list_display = ('name', 'price', 'count')


class CustomerAdmin(admin.ModelAdmin):
    list = ('name')
    list_display = ('name', 'address')
    pass

admin.site.register(Books, BookAdmin)
admin.site.register(Customer, CustomerAdmin)


