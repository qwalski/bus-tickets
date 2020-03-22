from base.models import TimeStampedModel
from django.db import models


class Constants:
    """
    Class for holding the constants variables
    """
    STATUS = (
        ("Open", "Open"),
        ("Close", "Close")
    )


class User(TimeStampedModel):
    """
    It holds the basic details of ticket owner
    """
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12, null=True)

    class Meta:
        app_label = "home"


class Ticket(TimeStampedModel):
    """
    It holds the ticket information like ticket status and owner of ticket
    """
    status = models.CharField(max_length=5, choices=Constants.STATUS, blank=True, null=True)
    user = models.ForeignKey(
        "User",
        related_name="ticket_user",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        app_label = "home"
