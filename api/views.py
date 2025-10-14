# from rest_framework import viewsets, generics, parsers
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import User, Feed, Comment, Report, FeedImage
# from .serializers import UserSerializer, FeedSerializer, CommentSerializer, ReportSerializer, FeedImageSerializer
# import cloudinary.uploader
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page

# # class RegisterView(generics.CreateAPIView):


# #     queryset = User.objects.all()

# #     serializer_class = UserSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         return Response(
#             {
#                 "message": "User registered successfully ✅",
#                 "username": user.username,
#                 "email": user.email,
#             },
#             status=status.HTTP_201_CREATED
#         )


# from rest_framework.exceptions import AuthenticationFailed
# from .serializers import CustomTokenObtainPairSerializer
# class LoginView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         # Catch the specific authentication error instead of a generic Exception
#         except AuthenticationFailed:
#             return Response(
#                 {"error": "Invalid username or password"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         tokens = serializer.validated_data
#         return Response({
#             "access": tokens["access"],
#             "refresh": tokens["refresh"],
#             "username": serializer.user.username,
#             "message": "Login successful ✅"
#         }, status=status.HTTP_200_OK)



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

# class FeedViewSet(viewsets.ModelViewSet):
#     queryset = Feed.objects.all()
#     serializer_class = FeedSerializer
#     permission_classes = [IsAuthenticated]
#     def get_permissions(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             return [AllowAny()]
#         return super().get_permissions()

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#     @method_decorator(cache_page(60 * 15))
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)




# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class ReportViewSet(viewsets.ModelViewSet):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
#     permission_classes = [IsAuthenticated]
#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)


# class FeedImageView(generics.CreateAPIView):
#     parser_classes = (parsers.MultiPartParser, parsers.FormParser)
#     serializer_class = FeedImageSerializer

#     def create(self, request, *args, **kwargs):
#         file = request.data.get('image')
#         feed_id = request.data.get('feed')
#         if not file or not feed_id:
#             return Response({'error': 'image and feed_id are required'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             feed = Feed.objects.get(id=feed_id)
#         except Feed.DoesNotExist:
#             return Response({'error': 'Feed not found'}, status=status.HTTP_404_NOT_FOUND)
#         upload_data = cloudinary.uploader.upload(file)
#         image_url = upload_data.get('url')
#         feed_image = FeedImage.objects.create(feed=feed, image_url=image_url)
#         serializer = self.get_serializer(feed_image)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


















# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login as auth_login
# from django.contrib import messages
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page

# from rest_framework import viewsets, generics, parsers, status
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.exceptions import AuthenticationFailed

# import cloudinary.uploader

# from .models import User, Feed, Comment, Report, FeedImage
# from .serializers import (
#     UserSerializer, FeedSerializer, CommentSerializer,
#     ReportSerializer, FeedImageSerializer, CustomTokenObtainPairSerializer
# )

# # ----------------- User Registration -----------------
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(
#             {
#                 "message": "User registered successfully ✅",
#                 "username": user.username,
#                 "email": user.email,
#             },
#             status=status.HTTP_201_CREATED
#         )

#     # Template view
#     def get(self, request):
#         return render(request, 'registration.html')


# # ----------------- User Login -----------------
# class LoginView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except AuthenticationFailed:
#             return Response(
#                 {"error": "Invalid username or password"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         tokens = serializer.validated_data
#         auth_login(request, serializer.user)  # Django session login
#         return Response({
#             "access": tokens["access"],
#             "refresh": tokens["refresh"],
#             "username": serializer.user.username,
#             "message": "Login successful ✅"
#         }, status=status.HTTP_200_OK)

#     # Template view
#     def get(self, request):
#         return render(request, 'login.html')


# # ----------------- User API & Template -----------------
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def list_template(self, request):
#         users = self.get_queryset()
#         return render(request, 'users.html', {'users': users})


# # ----------------- Feed API & Template -----------------
# class FeedViewSet(viewsets.ModelViewSet):
#     queryset = Feed.objects.all()
#     serializer_class = FeedSerializer
#     permission_classes = [IsAuthenticated]

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             return [AllowAny()]
#         return super().get_permissions()

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#     @method_decorator(cache_page(60 * 15))
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     def list_template(self, request):
#         feeds = self.get_queryset().order_by('-created_at')
#         return render(request, 'feeds.html', {'feeds': feeds})


# # ----------------- Comment API -----------------
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# # ----------------- Report API -----------------
# class ReportViewSet(viewsets.ModelViewSet):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)


# # ----------------- Feed Image Upload -----------------
# class FeedImageView(generics.CreateAPIView):
#     parser_classes = (parsers.MultiPartParser, parsers.FormParser)
#     serializer_class = FeedImageSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         file = request.data.get('image')
#         feed_id = request.data.get('feed')
#         if not file or not feed_id:
#             return Response({'error': 'image and feed_id are required'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             feed = Feed.objects.get(id=feed_id)
#         except Feed.DoesNotExist:
#             return Response({'error': 'Feed not found'}, status=status.HTTP_404_NOT_FOUND)

#         upload_data = cloudinary.uploader.upload(file)
#         image_url = upload_data.get('url')
#         feed_image = FeedImage.objects.create(feed=feed, image_url=image_url)
#         serializer = self.get_serializer(feed_image)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed

import cloudinary.uploader

from .models import User, Feed, Comment, Report, FeedImage
from .serializers import (
    UserSerializer, FeedSerializer, CommentSerializer,
    ReportSerializer, FeedImageSerializer, CustomTokenObtainPairSerializer
)

# ----------------- Home Page -----------------
def home(request):
    return render(request, 'home.html')


# ----------------- User Registration -----------------
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User registered successfully ✅",
            "username": user.username,
            "email": user.email,
        }, status=status.HTTP_201_CREATED)
    else:  # GET request -> render template
        return render(request, 'registration.html')


# ----------------- User Login -----------------
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        tokens = serializer.validated_data
        auth_login(request, serializer.user)
        return Response({
            "access": tokens["access"],
            "refresh": tokens["refresh"],
            "username": serializer.user.username,
            "message": "Login successful ✅"
        }, status=status.HTTP_200_OK)
    else:
        return render(request, 'login.html')


# ----------------- Users List -----------------
@login_required
def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


# ----------------- Feeds List -----------------
@login_required
def feeds_page(request):
    feeds = Feed.objects.all().order_by('-created_at')
    feed_data = []
    for feed in feeds:
        images = FeedImage.objects.filter(feed=feed)
        comments = Comment.objects.filter(feed=feed)
        feed_data.append({
            'feed': feed,
            'images': images,
            'comments': comments,
        })
    return render(request, 'feeds.html', {'feed_data': feed_data})


# ----------------- Create Feed -----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_feed(request):
    serializer = FeedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------- Comments -----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------- Reports -----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_report(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(reporter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------- Upload Feed Image -----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def feed_image_upload(request):
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
    serializer = FeedImageSerializer(feed_image)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
