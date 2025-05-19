from rest_framework import viewsets
from .models import Handbook, Folder, Document
from .serializers import HandbookSerializer, FolderSerializer, DocumentSerializer
from .services import upload_file_to_ragflow

class HandbookViewSet(viewsets.ModelViewSet):
    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        upload_file_to_ragflow(instance)
