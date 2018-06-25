from rest_framework import serializers
from .models import Wallpaper, WallpaperImage


class WallpaperImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallpaperImage
        fields = ('img', 'device')


class WallpaperSerializer(serializers.ModelSerializer):
    wallpaper_images = WallpaperImageSerializer(many=True, read_only=True)

    class Meta:
        model = Wallpaper
        fields = ('title', 'pin_code', 'wallpaper_images')
        read_only_fields = ('title', 'wallpaper_images')
