from django_filters import FilterSet, OrderingFilter
from .models import Product

class ProductFilter(FilterSet):
    ordering = OrderingFilter(
        fields=(
            ('price', 'price'),
            ('date', 'date'),
        )
    )

    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
            'date': ['gt', 'lt'],
            'category': ['exact'],
            'product_name': ['icontains'],
        }
