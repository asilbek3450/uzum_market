from django.urls import path
from .views import HomePageView, ProductPageView, ProductDetailView

urlpatterns = [
   path("", HomePageView, name='home'),
   path("products/", ProductPageView, name='product'),
   path("products/<int:pk>/", ProductDetailView, name='product_detail')
]