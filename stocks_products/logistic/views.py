from django_filters.rest_framework import DjangoFilterBackend, CharFilter, FilterSet
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class StockFilter(FilterSet):
    products = CharFilter(field_name='products')

    class Meta:
        model = Stock
        fields = '__all__'

class StockSearchFilter(SearchFilter):
    search_param = "products"


class StockPagination(PageNumberPagination):
    page_size = 3

class ProductPagination(PageNumberPagination):
    page_size = 3


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StockFilter
    search_fields = ['products__title', 'products__description']
    pagination_class = StockPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    pagination_class = ProductPagination
