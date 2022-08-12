from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Product as ProductModel
from .serializers import ProductSerializer
class ProductAPIView(APIView):
    def get(self, request):
        product_list = ProductModel.objects.filter(is_active=True)
        serialized_data = ProductSerializer(product_list).data
        
        return Response(serialized_data, status=status.HTTP_200_OK)