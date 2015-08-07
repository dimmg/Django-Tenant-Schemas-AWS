from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('domain_url', 'schema_name', 'name', 'description',
                  'created_on')
