from rest_framework import routers
from .views import StudyPostViewSet

router = routers.DefaultRouter()
router.register("studyposts", StudyPostViewSet)

urlpatterns = router.urls
