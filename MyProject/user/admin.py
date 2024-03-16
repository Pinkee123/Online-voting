from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("id","name","contact","email","message")
admin.site.register(contact,contactAdmin)


class partiesAdmin(admin.ModelAdmin):
    list_display = ("id","name", "ppic", "pdate")
admin.site.register(parties,partiesAdmin)

class signupAdmin(admin.ModelAdmin):

    list_display = ("aadhar","name", "gender", "mobile",'picture','city','state','passwd','age')
admin.site.register(signup,signupAdmin)

class voteAdmin(admin.ModelAdmin):
    list_display = ("aadhar","vparty", "vdate")
admin.site.register(vote,voteAdmin)

class upcomingelctionAdmin(admin.ModelAdmin):

    list_display = ("id","etitle", "edes", "edate",'city','state')
admin.site.register(upcomingelction,upcomingelctionAdmin)

