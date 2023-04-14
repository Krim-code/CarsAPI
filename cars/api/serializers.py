from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'manufacturers')


class ManufacturerSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    cars_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'country', 'cars_count')

    def get_cars_count(self, manufacturer):
        return manufacturer.cars.count()


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'name', 'manufacturer', 'year_start', 'year_end', 'comments_count')

    def get_comments_count(self, car):
        return car.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_email', 'car', 'created_at', 'comment_text')
