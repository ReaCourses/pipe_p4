from rest_framework import serializers
from shop.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'name',
            'description'
        ]

class ClothesSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Clothes
        fields = [
            'name',
            'description',
            'price',
            'size',
            'color',
            'photo',
            'create_date',
            'is_exists',
            'category',
            'collection'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'clothes'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'clothes',
            'order',
            'count',
            'discount'
        ]