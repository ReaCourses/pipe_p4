from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('clothes', ClothesViewSet, basename='clothes')
router.register('pos-order', PosOrderViewSet, basename='pos-order')
router.register('order', OrderViewSet, basename='order')
router.register('collection', CollectionViewSet, basename='collection')
router.register('category', CategoryViewSet, basename='category')
urlpatterns += router.urls
