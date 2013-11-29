from django.contrib import admin
from orderpizza.models import UnitOrder

class UnitOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'pizza', 'potracheno')
    list_filter = ('potracheno',)
    ordering = ('-potracheno',)
admin.site.register(UnitOrder, UnitOrderAdmin)
