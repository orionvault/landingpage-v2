from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import status

from mailing.mail_service import EmailSender

from .models import PresaleOrder
from .serializers import PresaleSerializer


class PresaleViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    create:
    Create a new presale order.
    Available currencies: 'usd', 'btc' or 'eth'.
    Available investor types: 'individual', 'investor' or 'fund'.
    """
    model = PresaleOrder
    serializer_class = PresaleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            presale = serializer.save()
            EmailSender.send_template_mail(EmailSender.TEMPLATE_REGISTRATION,
                                           {'presale': presale},
                                           EmailSender.SUBJECT_REGISTRATION,
                                           [presale.email])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
