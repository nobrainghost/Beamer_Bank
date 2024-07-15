from django.db import models
from django.conf import settings
import random
# Create your models here.
# class Account(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     account_balance=models.DecimalField(max_digits=10,decimal_places=2)
#     time_in_bank=models.PositiveIntegerField()
#     dependents=models.PositiveIntegerField()
#     credit_score=models.DecimalField(max_digits=5,decimal_places=2)
#     account_number=models.CharField(max_length=16)
    

#     def generate_random_account_number(self):
#         return ''.join(random.choices('0123456789BEAMER',k=16))
    
#     def save(self, *args, **kwargs):
#         self.account_number=self.generate_random_account_number()
#         super(Account,self).save(*args,**kwargs)

#     def __str__(self):
#         return f"{self.user.email} - {self.account_number}"
