from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

# url paths
urlpatterns = [
    # path("", views.index, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:pk>/", views.product, name="product"),
    path("register/", views.register, name="register"),
    path("login/", obtain_auth_token, name="login"),
]
