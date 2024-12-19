from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class HomeCarListAPIView(ListAPIView):
    queryset = Car.objects.only('id', 'images', 'category', 'title', 'price', 'currency', 'location',
                                'created_at').select_related('category').prefetch_related('images')
    serializer_class = HomeCarSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'price']
    ordering_fields = ['price']
    search_fields = ['title', 'category__title']


class CreateCarAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CreateCarSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            car_serializer = self.get_serializer(data=request.data)
            car_serializer.is_valid(raise_exception=True)
            car = car_serializer.save()

            # Получаем данные изображений из request.FILES
            images_data = request.FILES.getlist('images')

            # Предполагается, что вы уже создали эти фотографии и теперь просто связываете их с продуктом
            for image_data in images_data:
                car_image = Media.objects.create(file=image_data)
                car.images.add(car_image)  # Добавляем фотографию к продукту
            return Response({
                'success': car_serializer.data,
                'message': 'Car created'
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'error': str(e),
                'message': 'Ошибка при создания автомобиля .'
            }, status=status.HTTP_400_BAD_REQUEST)

    #  устанавливает автора перед сохранением объекта
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all().prefetch_related('images', 'author')
    serializer_class = CarDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CarCategoryAPIView(ListAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class TypeFuelAPIView(ListAPIView):
    queryset = TypeFuel.objects.all()
    serializer_class = TypeFuelSerializer


class BodyTypeAPIView(ListAPIView):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializer


class GearboxAPIView(ListAPIView):
    queryset = Gearbox.objects.all()
    serializer_class = GearboxSerializer


class MachineConditionAPIView(ListAPIView):
    queryset = MachineCondition.objects.all()
    serializer_class = MachineConditionSerializer


class MachineDriveAPIView(ListAPIView):
    queryset = MachineDrive.objects.all()
    serializer_class = MachineDriveSerializer


class ColorAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
