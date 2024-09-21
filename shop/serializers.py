from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', ]


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class RatingSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers()

    class Meta:
        model = Rating
        fields = ['user','stars']


class ReviewSerializers(serializers.ModelSerializer):
    author = UserProfileSimpleSerializers
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'parent_review', 'created_date']



class ProductPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    product = ProductPhotosSerializers(read_only=True, many=True)
    category = CategorySerializers
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product', 'category', 'price', 'average_rating', 'date']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    ratings = RatingSerializers(read_only=True, many=True)
    reviews = ReviewSerializers(read_only=True, many=True)
    product = ProductPhotosSerializers(read_only=True, many=True)
    date = serializers.DateField(format='%d-%m-%Y')
    average_rating = serializers.SerializerMethodField()
    owner = UserProfileSimpleSerializers()

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'product', 'product_video',
                  'active', 'average_rating', 'date', 'ratings', 'reviews', 'owner']


    def get_average_rating(self, obj):
        return obj.get_average_rating()



class CarItemSerializer(serializers.ModelSerializer):
    product = ProductSerializers(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = CarItem
        fields = ['id', 'product', 'product_id', 'quantity', 'get_total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CarItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']


    def get_total_price(self, obj):
        return obj.get_total_price()



