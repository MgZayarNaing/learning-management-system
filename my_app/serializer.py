from rest_framework import serializers
from my_app.models import *

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = "__all__"

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesModel
        fields = "__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionModel
        fields = "__all__"