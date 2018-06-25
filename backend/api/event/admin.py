from django.contrib import admin
from .models import Wallpaper, WallpaperImage


class WallpaperImageInline(admin.TabularInline):
    model = WallpaperImage


class AdminWallpaper(admin.ModelAdmin):
    list_display = ('id', 'title', 'pin_code', 'last_visit', 'created_at')
    inlines = (WallpaperImageInline,)

admin.site.register(Wallpaper, AdminWallpaper)
