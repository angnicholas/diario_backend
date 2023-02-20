from django.urls import path
from .views import (
    ListPatients,
    ListJournalEntriesByPatient,
)

urlpatterns = [
    path('patient/list/', ListPatients.as_view()),
    path('journalentries/<int:pk>/', ListJournalEntriesByPatient.as_view()),
]
