from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)