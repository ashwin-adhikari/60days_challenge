from django.contrib import admin
from django.urls import path, include

# from apps import views
from ordermanagement.views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = DefaultRouter()
router.register(r"tables", TableViewSet)
router.register(r"items", ItemViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"managers", ManagerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("apps.urls")),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name= "schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
