from .models import Ticket, User
from .serializers import TicketSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["PATCH"])
def update_ticket_status(request, ticket_id):
    """
    Updates ticket status and person details
    
    {form data}:
        - firstname
        - lastname
        - contact_number
        - status
    """
    if request.method == "PATCH":
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket does not exist"},
                status=status.HTTP_400_NOT_FOUND
            )

        if ticket.user is not None:
            user, created = User.objects.get_or_create(
                id=ticket.user.id
            )
        else:
            user = User.objects.create()

        if "status" in request.data:
            ticket.status = request.data["status"]
        if "firstname" in request.data:
            user.firstname = request.data["firstname"]
        if "lastname" in request.data:
            user.lastname = request.data["lastname"]
        if "contact_number" in request.data:
            user.contact_number = request.data["contact_number"]
        user.save()
        ticket.user = user
        ticket.save()
        response = {"status": "Successfully updated ticket status"}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_ticket_status(request, ticket_id):
    """
    Returns the ticket status
    {ticket_id} - Ticket ID among 40 tickets
    """
    if request.method == "GET":
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket does not exist"},
                status=status.HTTP_400_NOT_FOUND
            )
        response = {
            "ticket_status": ticket.status,
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_closed_tickets(request):
    """
    Returns the list of closed tickets
    """
    if request.method == "GET":
        closed_ticket_list = Ticket.objects.filter(status="Close")
        serializer = TicketSerializer(
            closed_ticket_list,
            many=True
        )
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_opened_tickets(request):
    """
    Returns the list of opened tickets
    """
    if request.method == "GET":
        opened_ticket_list = Ticket.objects.filter(status="Open")
        serializer = TicketSerializer(
            opened_ticket_list,
            many=True
        )
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_person_details(request, ticket_id):
    """
    Returns the person details of a particular ticket
    """
    if request.method == "GET":
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket does not exist"},
                status=status.HTTP_400_NOT_FOUND
            )
        serializer = TicketSerializer(ticket)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def reset_tickets(request):
    """
    Resets all the close tickets to open
    """
    if request.method == "PATCH":
        tickets = Ticket.objects.all()
        tickets.update(status="Open")
        response_data = {"status": "Successfully reset the tickets to open state"}
        return Response(response_data, status=status.HTTP_200_OK)
