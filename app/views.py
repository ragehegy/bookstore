from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *
from utils.renderers import JSONRenderer

class UsersView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReviewsView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def post(self, request, book_id):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BooksView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)