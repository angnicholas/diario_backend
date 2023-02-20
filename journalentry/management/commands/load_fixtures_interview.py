from django.core.management.base import BaseCommand
from authapi.models import User
from journalentry.models import JournalEntry
from ml_kit.compiler import SENTIMENT_PREDICTOR, SUMMARIZER
from glob import glob
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        hashword = 'pbkdf2_sha256$320000$CEJpLuAsuWmkDOu7Nc4rZL$+MSj/IQQjumeMZNtOr8z3lI0S0bSwLmGCtgHUJiLw8M='
        # test1234!

        User.objects.create(
            password=hashword,
            username='alex',
            display_name='Alex',
            role='TP',
        )

        User.objects.create(
            password=hashword,
            username='ben',
            display_name='Ben',
            role='PT',
            therapist=User.objects.get(pk=1),
        )

        # User.objects.create(
        #     password = hashword,
        #     username='charlie',
        #     display_name='Charlie',
        #     role='PT',
        #     therapist=User.objects.get(pk=1),
        # )

        with open('sample_data/new_sample_data/positive.txt', mode='r') as f:
            text = f.read()
            JournalEntry.objects.create(
                patient=User.objects.get(pk=2),
                title='I am happy',
                text=text,
                # date_created=datetime.datetime(2022, 9, 5, 12, 0, 0),
                # date_updated=datetime.datetime(2022, 9, 5, 12, 0, 0),
            )

        je = JournalEntry.objects.get(pk=1)
        # je.date_created = datetime()
        # je.date_updated  = datetime()
        # je.date_created = datetime.datetime(2022, 9, 5, 12, 0, 0)
        # je.date_updated = datetime.datetime(2022, 9, 5, 12, 0, 0)
        je.save()

        with open('sample_data/new_sample_data/neutral.txt', mode='r') as f:
            text = f.read()
            JournalEntry.objects.create(
                patient=User.objects.get(pk=2),
                title='Today was neutral',
                text=text,
                # date_created=datetime.datetime(2022, 9, 5, 12, 0, 0),
                # date_updated=datetime.datetime(2022, 9, 5, 12, 0, 0),
            )

        je = JournalEntry.objects.get(pk=1)
        # je.date_created = datetime()
        # je.date_updated  = datetime()
        # je.date_created = datetime.datetime(2022, 9, 5, 12, 0, 0)
        # je.date_updated = datetime.datetime(2022, 9, 5, 12, 0, 0)
        je.save()

        # with open('sample_data/for_demo/neutral4 (meeting denise).txt', mode='r') as f:
        #     text = f.read()
        #     JournalEntry.objects.create(
        #         patient=User.objects.get(pk=2),
        #         title='Meeting a childhood friend',
        #         text=text,
        #         date_created=datetime.datetime(2022, 9, 7, 12, 0, 0),
        #         date_updated=datetime.datetime(2022, 9, 7, 12, 0, 0)
        #     )

        # with open('sample_data/for_demo/neutral3 (covid).txt', mode='r') as f:
        #     text = f.read()
        #     JournalEntry.objects.create(
        #         patient=User.objects.get(pk=3),
        #         title='The Day I got Covid',
        #         text=text,
        #         date_created=datetime.datetime(2022, 9, 5, 12, 0, 0)
        #     )

        # with open('sample_data/for_demo/neutral1 (martial arts class).txt', mode='r') as f:
        #     text = f.read()
        #     JournalEntry.objects.create(
        #         patient=User.objects.get(pk=3),
        #         title='Learning Martial Arts',
        #         text=text,
        #         date_created=datetime.datetime(2022, 9, 7, 12, 0, 0)
        #     )

        # compute sentiment and summary
        for je in JournalEntry.objects.all():
            je.sentiment = SENTIMENT_PREDICTOR(je.text)
            je.summary = SUMMARIZER(je.text)
            je.save()
