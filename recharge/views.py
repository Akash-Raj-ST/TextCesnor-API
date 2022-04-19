from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import user


@api_view(["POST"])
def recharge(request):
    if "username" not in request.data:
        print("username REQ")
        return Response({"ERROR: USERNAME required"}, status=status.HTTP_400_BAD_REQUEST)
    
    for level in ["level1","level2","level3"]:
        if level not in request.data:
            print(request.data)
            print("level REQ");
            return Response({"ERROR: All levels required"},status=status.HTTP_400_BAD_REQUEST)
    
    username = request.data["username"]

    if user.objects.filter(username=username).exists():
        user_obj = user.objects.get(username=username)
        user_obj.level1 += int(request.data["level1"])
        user_obj.level2 += int(request.data["level2"])
        user_obj.level3 += int(request.data["level3"])

        user_obj.save()
        return Response({"Recharge successful"},status=status.HTTP_202_ACCEPTED)

    else:
        return Response({"ERROR: No such user exists"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_balance(request,username):
    if not user.objects.filter(username=username).exists():
        return Response({"User doesnt exist"}, status=status.HTTP_400_BAD_REQUEST)

    user_obj = user.objects.get(username=username)

    data = {
        "level1": user_obj.level1,
        "level2": user_obj.level2,
        "level3": user_obj.level3,
    }

    return Response(data, status=status.HTTP_202_ACCEPTED)
