from django.core.management.base import BaseCommand
from authapi.models import User
from journalentry.models import JournalEntry
from ml_kit.compiler import SENTIMENT_PREDICTOR, SUMMARIZER
from glob import glob
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        hashword = 'pbkdf2_sha256$320000$CEJpLuAsuWmkDOu7Nc4rZL$+MSj/IQQjumeMZNtOr8z3lI0S0bSwLmGCtgHUJiLw8M='
        #test1234!

        User.objects.create(
            password = hashword,
            username='alex',
            display_name='Alex',
            role='TP',
        )

        User.objects.create(
            password = hashword,
            username='ben',
            display_name='Ben',
            role='PT',
            therapist=User.objects.get(pk=1),
        )
        
        with open('sample_data/new_sample_data/positive.txt', mode='r') as f:
            text = f.read()
            JournalEntry.objects.create(
                patient=User.objects.get(pk=2),
                title='I am happy',
                text=text,
            )

        for i in range(15):
            with open('sample_data/new_sample_data/neutral.txt', mode='r') as f:
                text = f.read()
                JournalEntry.objects.create(
                    patient=User.objects.get(pk=2),
                    title='Today was neutral',
                    text=text,
                )
        
        with open('sample_data/new_sample_data/neutral_Verylong.txt', mode='r') as f:
            text = f.read()
            JournalEntry.objects.create(
                patient=User.objects.get(pk=2),
                title='Today was neutral',
                text=text,
            )

        #compute sentiment and summary
        for je in JournalEntry.objects.all():
            je.sentiment = SENTIMENT_PREDICTOR(je.text)
            je.summary = SUMMARIZER(je.text)
            je.save()





