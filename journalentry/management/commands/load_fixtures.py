from django.core.management.base import BaseCommand
from authapi.models import User
from journalentry.models import JournalEntry
from ml_kit.compiler import SENTIMENT_PREDICTOR, SUMMARIZER
from glob import glob

class Command(BaseCommand):
    def handle(self, *args, **options):
        hashword = 'pbkdf2_sha256$320000$CEJpLuAsuWmkDOu7Nc4rZL$+MSj/IQQjumeMZNtOr8z3lI0S0bSwLmGCtgHUJiLw8M='
        #test1234!

        User.objects.create(
            password = hashword,
            username='t1',
            display_name='ID 1 TP 1',
            role='TP',
        )

        User.objects.create(
            password = hashword,
            username='t2',
            display_name='ID 2 TP 2',
            role='TP',
        )

        User.objects.create(
            password = hashword,
            username='p1',
            display_name='ID 3 PT 1 (TP 1)',
            role='PT',
            therapist=User.objects.get(pk=1),
        )

        User.objects.create(
            password = hashword,
            username='p2',
            display_name='ID 4 PT 2 (TP 1)',
            role='PT',
            therapist=User.objects.get(pk=1),
        )

        User.objects.create(
            password = hashword,
            username='p3',
            display_name='ID 5 PT 3 (TP 2)',
            role='PT',
            therapist=User.objects.get(pk=2),
        )

        
        data = []

        for emotion in ['positive', 'neutral', 'negative']:
            for neg_text in glob(f'sample_data/{emotion}/*'):
                filepath = neg_text.split('/')[-1][:-4]
                with open(neg_text, mode='r') as f:
                    text = f.read()
                    data.append(
                        {'text':text,
                        'sentiment':emotion,
                        'title':filepath,
                        })

        for item in data:
            patient_number = \
                {'positive':3, 'neutral':4, 'negative':5}[item['sentiment']]
            
            JournalEntry.objects.create(
                patient=User.objects.get(pk=patient_number),
                title=item['title'],
                text=item['text'],                
            )

        #compute sentiment and summary
        for je in JournalEntry.objects.all():
            je.sentiment = SENTIMENT_PREDICTOR(je.text)
            je.summary = SUMMARIZER(je.text)
            je.save()





