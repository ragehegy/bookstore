from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    visible = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'visible',
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
    user_id = serializers.UUIDField(required=True, )
    content = serializers.CharField()

    class Meta:
        model = Review
        fields = (
            'user',
            'user_id',
            'content',
            'created',
            'updated_at',
        )

class BookSerializer(serializers.ModelSerializer):
    reviews = BookReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
