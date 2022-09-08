from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db.models import Max

from authapi.options import ROLE_LIST


MAX_LENGTH = 255

class UserManager(BaseUserManager):

    def create_user(self, username, display_name, password=None, **extra_fields):
        """Create user by username and password"""
        if not username:
            raise ValueError('User must have an email!')
        user = self.model(
            username=username,
            display_name=display_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    """Custom User model"""
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=MAX_LENGTH, unique = True)
    display_name = models.CharField(max_length=MAX_LENGTH)
    therapist = models.ForeignKey('User', on_delete=models.RESTRICT, blank=True, null=True) 
    #don't allow therapist to delete acct if they still have patients

    role = models.CharField(choices=ROLE_LIST, max_length=MAX_LENGTH, default="NN")
    # registered_institutions = models.ManyToManyField("self", blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    REQUIRED_FIELDS = ['role']
    
    @property
    def average_sentiment(self):
        from journalentry.models import JournalEntry
        tp, tn, cnt = 0, 0, 0
        for je in JournalEntry.objects.filter(patient=self.pk):
            tp += je.sentiment['positive']
            tn += je.sentiment['negative']
            cnt += 1
        if cnt == 0:
            return 0
        tp = tp / cnt
        tn = tn / cnt

        return tp - tn #positive - negative (-1 to 1)

    @property
    def latest_sentiment(self):
        from journalentry.models import JournalEntry
        je = JournalEntry.objects.filter(patient=self.pk).latest('date_updated')
        return je.sentiment['positive'] - je.sentiment['negative']

    @property
    def last_update(self):
        from journalentry.models import JournalEntry
        return JournalEntry.objects.filter(patient=self.pk).\
            aggregate(Max('date_updated'))['date_updated__max']
        
    def __str__(self):
        return f"{self.username!r}, {self.role}"

    def __repr__(self):
        return f"{self.username!r}, {self.role}"
