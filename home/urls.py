from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path(
        "update-ticket-status/<int:ticket_id>",
        views.update_ticket_status,
        name="update-ticket-status"
    ),
    path(
        "get-ticket-status/<int:ticket_id>",
        views.get_ticket_status,
        name="get-ticket-status"
    ),
    path(
        "closed-tickets/",
        views.get_closed_tickets,
        name="get-closed-tickets"
    ),
    path(
        "opened-tickets/",
        views.get_opened_tickets,
        name="get-opened-tickets"
    ),
    path(
        "person-details/ticket/<int:ticket_id>",
        views.get_person_details,
        name="get-person-details"
    ),
    path(
        "reset-tickets/",
        views.reset_tickets,
        name="reset-tickets"
    )
]