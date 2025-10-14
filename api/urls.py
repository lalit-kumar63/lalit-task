# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, FeedViewSet, CommentViewSet, ReportViewSet, RegisterView, LoginView, FeedImageView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'feeds', FeedViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'reports', ReportViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('auth/register/', RegisterView.as_view(), name='register'),
#     path('auth/login/', LoginView.as_view(), name='login'),
#     path('feeds/upload-image/', FeedImageView.as_view(), name='feed-image-upload'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Authentication pages
    path('register/', views.register_view, name='register_page'),  # template + API
    path('login/', views.login_view, name='login_page'),           # template + API

    # Users page
    path('users/', views.users_page, name='users_page'),

    # Feeds page
    path('feeds/', views.feeds_page, name='feeds_page'),

    # API endpoints
    path('auth/register/', views.register_view, name='api_register'),
    path('auth/login/', views.login_view, name='api_login'),
    path('auth/feeds/create/', views.create_feed, name='api_create_feed'),
    path('auth/comments/create/', views.create_comment, name='api_create_comment'),
    path('auth/reports/create/', views.create_report, name='api_create_report'),
    path('auth/feeds/upload-image/', views.feed_image_upload, name='api_feed_image_upload'),
]
