from rest_framework.generics import (
    ListAPIView,
)
from rest_framework import status
from rest_framework.response import Response

from authapi.models import User
from authapi.serializers import UserSerializer
from authapi.permissions import IsTherapist

from journalentry.models import JournalEntry
from journalentry.serializers import JournalEntrySerializer

class ListPatients(ListAPIView):
    permission_classes = [IsTherapist]
    def get(self, request, **kwargs):
        my_patients = User.objects.filter(therapist=request.user.pk)
        serializer = UserSerializer(my_patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListJournalEntriesByPatient(ListAPIView):
    permission_classes = [IsTherapist]
    def get(self, request, **kwargs):
        journal_entries = JournalEntry.objects.filter(patient=kwargs['pk'])
        serializer = JournalEntrySerializer(journal_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
