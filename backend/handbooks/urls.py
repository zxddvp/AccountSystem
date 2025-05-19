from rest_framework.routers import DefaultRouter
from .views import HandbookViewSet, FolderViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'handbooks', HandbookViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = router.urls
