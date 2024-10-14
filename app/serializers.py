from rest_framework import serializers

from .models import *

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
    user = UserSerializer()

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'content',
            'created',
            'updated_at'
        )
        
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
