from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rule_detect.models import *

# Create your views here.
class FetchDataAPIView(APIView):
    permission_classes = []

    def post(self, request):
        name = request.data.get("name")
        "write view releated logic here"
        return Response({"message": "User Unblocked Successfully"}, status=status.HTTP_200_OK)
