from re import L
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import JournalEntrySerializer
from .models import JournalEntry

from journalentry.utils.ml_dispatch import populate_ml_fields

class CreateJournalEntry(CreateAPIView):
    # permission_classes = [] #please update
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

    def post(self, request, *args, **kwargs):
        #do something
        request = populate_ml_fields(request)
        return super().post(request, *args, **kwargs)

class ListJournalEntry(ListAPIView):

    def get(self, request, **kwargs):
        
        queryset = JournalEntry.objects.filter(patient=request.user.pk)
        serializer = JournalEntrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleJournalEntry(RetrieveAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class DeleteJournalEntry(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class UpdateJournalEntry(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle]
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

    def patch(self, request, *args, **kwargs):
        #do something
        request = populate_ml_fields(request)
        return super().patch(request, *args, **kwargs)

class ComputeSentiment(GenericAPIView):
    def post(self, request, format=None):
        pass