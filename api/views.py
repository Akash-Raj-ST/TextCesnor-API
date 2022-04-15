from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["POST"])
def text_censor_level1(request):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)
    
    content = request.data["content"]

    return Response({f"Thanks for choosing level1 for {content}"})


@api_view(["POST"])
def text_censor_level2(request):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)

    content = request.data["content"]

    return Response({f"Thanks for choosing level2 for {content}"})


@api_view(["POST"])
def text_censor_level3(request):
    # validate request
    if "content" not in request.data:
        return Response({"content must be included"}, status=status.HTTP_400_BAD_REQUEST)

    content = request.data["content"]

    return Response({f"Thanks for choosing level3 for {content}"})

