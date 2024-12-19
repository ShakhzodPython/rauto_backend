from rest_framework import serializers

from .models import *
from media.models import Media
from media.serializers import UploadMediaSerializer


class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = ('id', 'title')
        read_only_fields = fields


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'title')
        read_only_fields = fields


class GearboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gearbox
        fields = ('id', 'title')
        read_only_fields = fields


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'title')
        read_only_fields = fields


class TypeFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFuel
        fields = ('id', 'title')
        read_only_fields = fields


class MachineConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineCondition
        fields = ('id', 'title')
        read_only_fields = fields


class MachineDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineDrive
        fields = ('id', 'title')
        read_only_fields = fields


class HomeCarSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    images = UploadMediaSerializer(many=True)
    created_at = serializers.DateTimeField(format='%d.%m.%Y')

    class Meta:
        model = Car
        fields = ('id', 'images', 'category', 'title', 'price', 'currency', 'location', 'created_at')
        read_only_fields = fields


class CreateCarSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.FileField(), write_only=True)

    # serializers.CurrentUserDefault() устанавливает автора на текущего пользователя
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = ('images', 'category', 'title', 'body_type', 'price', 'currency', 'mileage',
                  'year', 'gearbox', 'color', 'engine', 'type_fuel',
                  'machine_condition', 'machine_drive', 'desc', 'location', 'author')
        write_only_fields = ('images',)

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        car = Car.objects.create(**validated_data)
        for image_data in images_data:
            Media.objects.create(file=image_data)
            car.images.add(Media.objects.create(file=image_data))
        return car


class CarDetailSerializer(serializers.ModelSerializer):
    images = UploadMediaSerializer(many=True, required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=CarCategory.objects.all(), source='category.title')
    title = serializers.CharField()
    body_type = serializers.PrimaryKeyRelatedField(queryset=BodyType.objects.all(), source='body_type.title')
    year = serializers.IntegerField()
    gearbox = serializers.PrimaryKeyRelatedField(queryset=Gearbox.objects.all(), source='gearbox.title')
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), source='color.title')
    engine = serializers.CharField()
    type_fuel = serializers.PrimaryKeyRelatedField(queryset=TypeFuel.objects.all(), source='type_fuel.title')
    machine_condition = serializers.PrimaryKeyRelatedField(queryset=MachineCondition.objects.all(),
                                                           source='machine_condition.title')
    desc = serializers.CharField()
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Car
        fields = ('images', 'category', 'title', 'body_type', 'year', 'gearbox',
                  'color', 'engine', 'type_fuel', 'machine_condition',
                  'desc', 'author')

    # Обновление объекта
    def update(self, instance, validated_data):
        fields = ['title', 'year', 'engine', 'desc']
        for field in fields:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))

        # Обработка полей ForeignKey
        foreign_key_fields = ['category', 'body_type', 'gearbox', 'color', 'type_fuel', 'machine_condition']
        for field in foreign_key_fields:
            model = getattr(instance, field).__class__
            field_data = validated_data.get(field)
            if field_data:
                field_instance, created = model.objects.get_or_create(title=field_data['title'])
                setattr(instance, field, field_instance)

        # Обработка поля images
        images_data = validated_data.pop('images', [])
        instance.images.clear()
        for image_data in images_data:
            image_instance = Media.objects.create(**image_data)
            instance.images.add(image_instance)

        instance.save()
        return instance
