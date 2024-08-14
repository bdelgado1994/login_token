from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView

from login.views import TaskViewSet

app_name="login"

router=routers.DefaultRouter()
router.register(r"task",TaskViewSet)

urlpatterns=[
    path("schema/",SpectacularAPIView.as_view(),name="schema"),
    path("schema/swagger/",SpectacularSwaggerView.as_view(url_name="login:schema"),name="swagger"),
    path("token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("token/verify/",TokenVerifyView.as_view(),name="token_verify"),
    path("",include(router.urls))
]
