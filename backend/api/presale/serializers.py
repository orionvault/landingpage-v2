from rest_framework import serializers
from .models import PresaleOrder


class PresaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresaleOrder
        fields = ('first_name', 'last_name', 'residency', 'email',
                  'currency', 'contribution', 'investor_type')
        read_only_fields = ('updated_at', 'created_at')
