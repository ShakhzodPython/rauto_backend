from rest_framework import serializers

from .models import Media


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        # Постараемся получить абсолютный URL-адрес файла
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://localhost:8000" + str(media.file.url)


class UploadMediaSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True, required=True)

    class Meta:
        model = Media
        fields = ('id', 'file')
        read_only = ('id',)

