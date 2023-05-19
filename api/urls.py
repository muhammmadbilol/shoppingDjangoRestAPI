from django.urls import path, include
from .views import CartAddProductView

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('categories/', views.CategoryListCreateAPIView.as_view(), name='categories_api'),
    path('products/', views.ProductListCreateAPIView.as_view(), name='products_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cart/', CartAddProductView.as_view(), name='cart-add-products'),

]
