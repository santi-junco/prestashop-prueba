from rest_framework import generics, filters
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductCreateView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['precio']

    def get_queryset(self):
        products = Producto.objects.all()
        name = self.request.query_params.get('nombre', None)
        price = self.request.query_params.get('precio', None)

        if name is not None:
            products = products.filter(name__icontains=name)

        if price is not None:
            products = products.filter(price=price)

        return products
