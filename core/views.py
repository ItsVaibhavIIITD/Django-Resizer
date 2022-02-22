from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from core.serializers import RecordSerializer
from core.models import Record, BackgroundJob
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def add_record(request):
    """
    Add a new record to the database
    """
    print(request.data)
    serializer = RecordSerializer(data = request.data)

    if serializer.is_valid():
        record = serializer.save()
        record.image = request.data.get("image") or record.image
        record.save()
        BackgroundJob.objects.create(
            record = record
        )
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(["GET"])
def records(request):
    """
    List all the records
    """
    records = Record.objects.order_by("-timestamp")
    serializer = RecordSerializer(records, context = {"request": request},  many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)