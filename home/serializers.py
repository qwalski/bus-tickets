from .models import Ticket, User
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for ticket status and ticket owner details
    """
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    contact_number = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ("status", "firstname", "lastname", "contact_number")


    def get_firstname(self, obj):
        return obj.user.firstname if obj.user is not None else None

    def get_lastname(self, obj):
        return obj.user.lastname if obj.user is not None else None

    def get_contact_number(self, obj):
        return obj.user.contact_number if obj.user is not None else None
