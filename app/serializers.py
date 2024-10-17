from django.utils.html import strip_tags
from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    is_active = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'is_active',
            'created_at',
            'updated_at'
        )

# class ReviewSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True, )
#     user_id = serializers.UUIDField(required=True, )
#     book_id = serializers.UUIDField(required=True, )

#     def create(self, validated_data):
#         return super().create(validated_data)

#     class Meta:
#         model = Review
#         fields = (
#             'user',
#             'content',
#             'created',
#             'updated_at',
#             'user_id',
#             'book_id'
#         )

class ReviewUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
        )

class BookReviewSerializer(serializers.ModelSerializer):
    user = ReviewUserSerializer(read_only=True)
    book_id = serializers.UUIDField(write_only=True)
    user_id = serializers.UUIDField(required=True, )
    content = serializers.CharField()

    class Meta:
        model = Review
        fields = (
            'user',
            'user_id',
            'book_id',
            'content',
            'created',
            'updated_at',
        )
    
    def validate_content(self, value):
        return strip_tags(value)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(BookSerializer):
    reviews = BookReviewSerializer(many=True, read_only=True)
