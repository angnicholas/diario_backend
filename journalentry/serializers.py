from rest_framework import serializers
from .models import JournalEntry


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'
        read_only_fields = ('date_created', 'date_updated')
