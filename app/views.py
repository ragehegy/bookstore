from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .serializers import *
from utils.renderers import JSONRenderer


class UsersView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = UserSerializer
    queryset = User.objects
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs["pk"])

    # def create(self, request):
    #     data = request.data

    #     serializer = self.serializer_class(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    throttle_classes = [UserRateThrottle]
    renderer_classes = (JSONRenderer,)
    serializer_class = BookReviewSerializer
    queryset = Review.objects.select_related("user")

    def create(self, request, pk):
        data = request.data
        data["book_id"] = pk

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk):
        query = self.queryset.filter(book__id=pk)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)



class BooksView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    renderer_classes = (JSONRenderer,)
    serializer_class = BookSerializer
    queryset = Book.objects.prefetch_related("reviews")

    def create(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailsSerializer
        else:
            return BookSerializer
