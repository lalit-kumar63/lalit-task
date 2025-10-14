from rest_framework import serializers
from .models import User, Feed, FeedImage, Comment, Report, Logging

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT serializer that adds username and message."""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Include custom fields in token payload
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['message'] = "Login successful ✅"
        return data

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImage
        fields = ('id', 'image_url', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    # 'author' is read-only because it's set automatically from the logged-in user
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        # Add 'feed' to this tuple so the serializer accepts it from the request
        fields = ('id', 'text_content', 'author', 'feed', 'created_at', 'updated_at')
class FeedSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    images = FeedImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = ('id', 'text_content', 'is_hidden', 'author', 'images', 'comments', 'created_at', 'updated_at')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'reporter', 'feed', 'created_at')

class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logging
        fields = '__all__'