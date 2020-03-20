from .models import Ticket, User
from django.contrib import admin


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("status", "user")


@admin.register(User)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "contact_number")
