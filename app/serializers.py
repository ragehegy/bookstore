from rest_framework import serializers

from .models import *

class BookSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'visible',
            'created',
            'updated_at'
        )

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, )
    user_id = serializers.UUIDField(required=True, )
    book_id = serializers.UUIDField(required=True, )

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'content',
            'created',
            'updated_at',
            'user_id',
            'book_id'
        )