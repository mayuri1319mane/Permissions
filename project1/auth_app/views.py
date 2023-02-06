from rest_framework.generics import CreateAPIView
from .Serializers import Userserializer


class UserAPI(CreateAPIView):
    serializer_class=Userserializer