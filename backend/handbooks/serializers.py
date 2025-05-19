from rest_framework import serializers
from .models import Handbook, Folder, Document

class HandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbook
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
