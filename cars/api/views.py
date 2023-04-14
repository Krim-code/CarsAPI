from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello!</h1>')


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def manufacturers(self, request, pk=None):
        country = self.get_object()
        manufacturers = Manufacturer.objects.filter(country=country)
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def country(self, request, pk=None):
        manufacturer = self.get_object()
        country = manufacturer.country
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def cars(self, request, pk=None):
        manufacturer = self.get_object()
        cars = Car.objects.filter(manufacturer=manufacturer)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def manufacturer(self, request, pk=None):
        car = self.get_object()
        manufacturer = car.manufacturer
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        car = self.get_object()
        comments = Comment.objects.filter(car=car)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(email_author=self.request.user.email)
