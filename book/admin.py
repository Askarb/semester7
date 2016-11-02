from django.contrib import admin
from book.models import *


class BookAdmin(admin.ModelAdmin):
    list = ('name')
    list_display = ('name','author', 'price', 'count')


class CustomerAdmin(admin.ModelAdmin):
    list = ('name')
    list_display = ('name', 'address', 'book_id')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'position', 'team_id')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    filter_horizontal = ('cources',)


class CourceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('model', 'company')


admin.site.register(Books, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Teams, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourceAdmin)
admin.site.register(Phone, PhoneAdmin)


