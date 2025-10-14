from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FeedViewSet, CommentViewSet, ReportViewSet, RegisterView, LoginView, FeedImageView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'feeds', FeedViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('feeds/upload-image/', FeedImageView.as_view(), name='feed-image-upload'),
]