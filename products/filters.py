import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    user_username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['title', 'user_username', 'content']