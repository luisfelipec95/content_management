from rest_framework.viewsets import ModelViewSet
from core.models import Category
from core.serializers import CategorySerializer

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer