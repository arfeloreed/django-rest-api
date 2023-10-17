from django.urls import path

from . import views

# url paths
urlpatterns = [
    # path("", views.index, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:pk>/", views.product, name="product"),
]
