from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
]   