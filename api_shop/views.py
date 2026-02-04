from django.shortcuts import render
from .serializers import *
from .permission import *
from rest_framework import viewsets
from rest_framework import mixins
from shop.models import *
from rest_framework.renderers import AdminRenderer

class ClothesViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                    #  mixins.CreateModelMixin,
                    #  mixins.UpdateModelMixin,
                    #  mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage
    renderer_classes = [AdminRenderer]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage