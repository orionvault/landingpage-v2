import logging

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import status
from django.utils import timezone

from .models import Wallpaper
from .serializers import WallpaperSerializer

logger = logging.getLogger('django')


class WallpaperViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    retrieve:
    Get details of the wallpaper.
    """
    model = Wallpaper
    serializer_class = WallpaperSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            wallpaper = self.model.objects.get(pin_code=pk)
            wallpaper.last_visit = timezone.now()
            wallpaper.save()

            logger.info('Wallpaper with PIN ' + str(pk) + ' visited')

            serializer = self.serializer_class(wallpaper,
                                               context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            logger.info('Wallpaper with PIN ' + str(pk) + ' not found')
            return Response('Wallpaper not found', status=status.HTTP_404_NOT_FOUND)
