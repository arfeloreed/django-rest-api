from rest_framework import serializers

from .models import Product


# model serializers
# product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price"]
