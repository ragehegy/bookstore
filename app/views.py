from django.http import HttpResponse
from rest_framework import viewsets

from serializers import *
from utils.renderers import JSONRenderer

class UsersView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = UserSerializer

class ReviewsView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = ReviewSerializer

class BooksView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = BookSerializer
