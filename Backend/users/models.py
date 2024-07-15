from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    username=None
    phone=models.CharField(max_length=255,unique=True)
    account_number=models.CharField(max_length=16,unique=True,default='0000000000000000')
    account_balance=models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    credit_score=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def generate_random_account_number(self):
        return ''.join(random.choices('0123456789BEAMER',k=16))
    def save(self, *args, **kwargs):
        self.account_number=self.generate_random_account_number()
        super(User,self).save(*args,**kwargs)

    @property
    def time_in_bank(self):
        now=timezone.now()
        account_created=self.date_joined
        time_difference=now-account_created
        return time_difference.days

    def __str__(self):
        return self.email