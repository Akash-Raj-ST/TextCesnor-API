from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import user

def check_valid(api_key):
    if user.objects.filter(api_key=api_key).exists():
        return user.objects.get(api_key=api_key)
    return None

def available_balance(user_id,level):
    user_obj = user.objects.get(user_id=user_id)
    if level==1:
        if user_obj.level1 >=1: return True
    if level==2:
        if user_obj.level2 >=1: return True
    if level == 3:
        if user_obj.level3 >= 1: return True

    return False

# Create your views here.
@api_view(["POST"])
def text_censor_level1(request,api_key):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)
    
    content = request.data["content"]

    user_obj = check_valid(api_key)
    if user_obj:
        if available_balance(user_id=user_obj.user_id, level=1):
            print("processing")
            user_obj.level1 -= 1
            user_obj.save()
            return Response(content, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"No available balance"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"No such user"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({f"Thanks for choosing level1 for {content}"})


@api_view(["POST"])
def text_censor_level2(request,api_key):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)

    content = request.data["content"]


    user_obj = check_valid(api_key)
    if user_obj:
        if available_balance(user_id=user_obj.user_id, level=2):
            print("processing")
            user_obj.level2 -= 1
            user_obj.save()
            return Response(content, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"No available balance"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"No such user"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def text_censor_level3(request,api_key):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)

    content = request.data["content"]


    user_obj = check_valid(api_key)
    if user_obj:
        if available_balance(user_id=user_obj.user_id,level=3):
            print("processing")
            user_obj.level3 -= 1
            user_obj.save()
            return Response(content, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"No available balance"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"No such user"}, status=status.HTTP_400_BAD_REQUEST)


