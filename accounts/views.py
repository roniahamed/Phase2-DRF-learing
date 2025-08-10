from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from .models import User
from rest_framework.permissions import AllowAny


class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response({'message':'Registration Successfully'}, status=status.HTTP_201_CREATED, headers=headers)
