from django.contrib import admin
from core.models import Waiting

class WaitingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Waiting, WaitingAdmin)
