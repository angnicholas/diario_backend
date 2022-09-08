# urls.py

from django.urls import path
from .views import (
    CreateJournalEntry,
    ListJournalEntry,
    SingleJournalEntry,
    SingleJournalEntry,
    DeleteJournalEntry,
    UpdateJournalEntry,
)

urlpatterns = [
   path('create/', CreateJournalEntry.as_view()),
   path('list/', ListJournalEntry.as_view()),
   path('<int:pk>/', SingleJournalEntry.as_view()),
   path('<int:pk>/delete/', DeleteJournalEntry.as_view()),
   path('<int:pk>/update/', UpdateJournalEntry.as_view()),
]