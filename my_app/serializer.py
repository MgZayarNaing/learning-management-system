from rest_framework import serializers
from my_app.models import *

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = "__all__"