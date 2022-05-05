from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import FileUpload, Client, Organization, Bills


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bills
        fields = '__all__'
        depth = 3
