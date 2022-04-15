from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def login(request):
    print("login")
    return Response({"Login page"},status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
def register(request):
    print("Register")
    return Response({"Register page"}, status=status.HTTP_202_ACCEPTED)
