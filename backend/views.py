from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializer, SelfSerializer

class UserCreateView(APIView):
  permission_classes = [AllowAny]
  
  def post(self, reuqest):
    serializer = CreateUserSerializer(data=reuqest.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({"message": "user Create"}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
  permission_classes = (IsAuthenticated,)

  def get(slef, request):
    serializer = SelfSerializer(request.user)
    return Response(serializer.data)