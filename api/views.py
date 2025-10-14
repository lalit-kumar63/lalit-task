from rest_framework import viewsets, generics, parsers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Feed, Comment, Report, FeedImage
from .serializers import UserSerializer, FeedSerializer, CommentSerializer, ReportSerializer, FeedImageSerializer
import cloudinary.uploader
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# class RegisterView(generics.CreateAPIView):


#     queryset = User.objects.all()

#     serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully ✅",
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class LoginView(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
#         tokens = serializer.validated_data
#         return Response({
#             "access": tokens["access"],
#             "refresh": tokens["refresh"],
#             "username": serializer.user.username,
#             "message": "Login successful ✅"
#         }, status=status.HTTP_200_OK)
from rest_framework_simplejwt.serializers import CustomTokenObtainPairSerializer
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = serializer.validated_data
        return Response({
            "access": tokens["access"],
            "refresh": tokens["refresh"],
            "username": serializer.user.username,
            "message": "Login successful ✅"
        }, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)




class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class FeedImageView(generics.CreateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    serializer_class = FeedImageSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get('image')
        feed_id = request.data.get('feed')
        if not file or not feed_id:
            return Response({'error': 'image and feed_id are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            feed = Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            return Response({'error': 'Feed not found'}, status=status.HTTP_404_NOT_FOUND)
        upload_data = cloudinary.uploader.upload(file)
        image_url = upload_data.get('url')
        feed_image = FeedImage.objects.create(feed=feed, image_url=image_url)
        serializer = self.get_serializer(feed_image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)