from django.urls import include, path
from . import views
from .views import SignupView, SigninView, SignoutView, ChangePasswordView, FollowView, UnfollowView, UserFollowListView
urlpatterns = [
    path('', views.SignupView.as_view()),
    path('login/', views.SigninView.as_view()),
    path('logout/', views.SignoutView.as_view()),
    path('password/', ChangePasswordView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
    # 팔로우 및 언팔로우 엔드포인트
    path('<str:username>/follow', FollowView.as_view()),
    path('<str:username>/unfollow', UnfollowView.as_view()),
    path('<str:username>/follow-list', UserFollowListView.as_view()),
]
