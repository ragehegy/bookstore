from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .serializers import UserSerializer, LoginSerializer, LogoutSerializer
from utils.renderers import JSONRenderer


class Registration(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [AnonRateThrottle]
    renderer_classes = (JSONRenderer,)
    serializer_class = UserSerializer

    def post(self, request):
        user = request.data.get("user", {})

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Login(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [AnonRateThrottle]
    renderer_classes = (JSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Logout(APIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
