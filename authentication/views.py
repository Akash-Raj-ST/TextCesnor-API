from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import user
from .serializer import UserSerializer
from .password import KEY

import string
import random


def encrypt(password):
    enc = KEY.encrypt(bytes(password, "utf-8"))
    return enc.decode("utf-8")


def decrypt(password):
    dec = KEY.decrypt(bytes(password, "utf-8"))
    return dec.decode("utf-8")

def generate_api():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res

@api_view(["POST"])
def login(request):
    print("processing login....")

    if "username" and "password" not in request.data:
        return Response({"Wrong Format"}, status=status.HTTP_400_BAD_REQUEST)
    
    username = request.data['username']
    password = request.data['password']
    
    
    user_obj = user.objects.filter(username=username)

    if user_obj.exists():

        user_obj = user.objects.get(username=username)
        ret_pass = user_obj.password

        if decrypt(ret_pass) == password:
            user_id = user_obj.user_id
            api_key = user_obj.api_key

            data = {
                "message": "Login Successful",
                "user_id": user_id,
                "username":user_obj.username,
                "api_key": api_key,
            }

            print("Login successful")
            return Response(data, status=status.HTTP_202_ACCEPTED)

        data = {"message": "Wrong password"}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    return Response({"No such user"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def register(request):
    print("Register")
    #validate request
    if "username" and "email" and "password" in request.data:
        username = request.data['username']
        email = request.data['email']
        request.data._mutable = True
        request.data['password'] = encrypt(request.data['password'])
    
    else:
        return Response({"Wrong Format"},status=status.HTTP_400_BAD_REQUEST)

    msgs = []

    if user.objects.filter(username=username).exists():
        msgs.append("Username Taken")
        
    if user.objects.filter(email=email).exists():
        msgs.append("Email already used")

    if len(msgs)>0:
        data = {"message": msgs}

    else:
        while(True):
            api_key = generate_api()
            if(not user.objects.filter(api_key=api_key).exists()):
                break
        
        request.data["api_key"] = api_key
        serializer = UserSerializer(data=request.data)
        request.data._mutable = False

        if serializer.is_valid():
            serializer.save()
            user_obj = user.objects.get(username=username)

            

            data = {
                "message": "Account created Successfully",
                "user_id": user_obj.user_id, 
                "username": user_obj.username,
                "api_key": api_key,
                }

            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {"message": "Not Valid"}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)
