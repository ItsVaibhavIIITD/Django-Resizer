from rest_framework import status
from core.utils import resize_job, resize
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
    serializer = RecordSerializer(data = request.data)

    if serializer.is_valid():
        record = serializer.save()
        record.image = request.data.get("image") or record.image
        record.save()
        BackgroundJob.objects.create(
            record = record
        )
        return Response(RecordSerializer(instance = record, context = {"request": request}).data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(["POST"])
def resize_records(request):
    """
    Resize all the pending records
    """
    records_ids = resize_job()
    return Response({"ids": records_ids}, status = status.HTTP_200_OK)
        
@api_view(["POST"])
def resize_record(request, id):
    """
    Resize a specific record
    """
    record = Record.objects.filter(pk = id)

    if not record.exists():
        return Response({"error": "Invalid record id."}, status = status.HTTP_204_NO_CONTENT)
    
    resize(record.first())
    return Response({"id": id}, status = status.HTTP_200_OK)

@api_view(["GET"])
def records(request):
    """
    List all the records
    """
    records = Record.objects.order_by("-timestamp")
    serializer = RecordSerializer(records, context = {"request": request},  many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)