from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from products.views import ProductViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'', ProductViewSet)

urlpatterns = router.urls
