from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User,Transactions
import jwt,datetime
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import transaction
from decimal import Decimal
import random


# Create your views here.
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        def generate_random_account_number(self):
         return ''.join(random.choices('0123456789',k=16))
        request=request.data
        request['account_number']=generate_random_account_number(self)
        serializer=UserSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload={
        'id':user.id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=6000),
        'iat':datetime.datetime.utcnow()
         }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response()

        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token}

        return response


class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            print(token)
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            print(token)
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user=User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)
        return Response(serializer.data)
  

class LogoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }
        return response

class DepositView(APIView):
    
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user=User.objects.filter(id=payload['id']).first()
        amount=request.data['amount']
        amount=Decimal(amount)
        receiver='Self'
        if amount<=0:
            return Response({'message':'Amount must be greater than 0'})
        transaction_date=datetime.datetime.now()
        Transactions.objects.create(user=user,transaction_status=True ,transaction_type='deposit',receiver=receiver, amount=amount,transaction_date=transaction_date)
        user.account_balance=user.account_balance+amount
        user.save()
        return Response({'message':'success'})
    

class WithdrawView(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user=User.objects.filter(id=payload['id']).first()
        amount=request.data['amount']
        amount=Decimal(amount)
        receiver=self
        account_balance=user.account_balance
        if amount>account_balance:
            return Response({'message':'Insufficient balance'})
        Transactions.objects.create(user=user,transaction_status=True,receiver=receiver ,transaction_type='withdraw',amount=amount,transaction_date=datetime.datetime.now())
        user.account_balance=account_balance-amount
        user.save()
        return Response(f'Amount withdrawn successfully {amount}, balance : {user.account_balance}')  


class TransactionListView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user=User.objects.filter(id=payload['id']).first()
        serializer=TransactionSerializer(user.transactions_set.all(),many=True)
        return Response(serializer.data)           
    


class SendView(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        sender=User.objects.filter(id=payload['id']).first()
        amount=request.data['amount']
        amount=Decimal(amount)
        receiver=request.data['receiver_account_number']
        if receiver==None:
            return Response({'message':'Receiver account number is required'})
        print(receiver)
        receivee=User.objects.filter(account_number=receiver).first()
        if amount>sender.account_balance:
            return Response({'message':'Insufficient balance'})
        if receivee==sender:
            return Response({'message':'Cannot send money to yourself'})
        if receivee!=None:
            print(receivee)
            sender.account_balance=sender.account_balance-amount
            receivee.account_balance=receivee.account_balance+amount
            Transactions.objects.create(user=sender,transaction_status=True,receiver=receiver ,transaction_type='withdraw',amount=amount,transaction_date=datetime.datetime.now())
            Transactions.objects.create(user=receivee,transaction_status=True,receiver=sender.account_number ,transaction_type='deposit',amount=amount,transaction_date=datetime.datetime.now())
            sender.save()
            receivee.save()

            return Response({'message':'Internal Transfer successful'})
        else:
            print("A Transfer To an External Bank")
            sender.account_balance=sender.account_balance-amount
            Transactions.objects.create(user=sender,transaction_status=True,receiver=receiver ,transaction_type='withdraw',amount=amount,transaction_date=datetime.datetime.now())
            sender.save()
            return Response({'message':'External Transfer successful'})
