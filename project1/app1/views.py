from rest_framework.views import APIView
from .Serializers import MobileSerializers
from .models import Mobile
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class MobileAPIView(APIView):

    serializer_class = MobileSerializers
    model_class = Mobile
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]

def get(self, request):
    fetched = self.model_class.objects.all()
    serializer = self.serializer_class(fetched, many=True)
    return Response(data=serializer.data)

def post(self, request):
    serializer = self.serializer_class(data=request.data, context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response(data=serializer.errors)

class MobileDetailGenricView(RetrieveUpdateDestroyAPIView):
    serializer_class = MobileSerializers
    queryset = Mobile
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]


