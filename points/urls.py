from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import InsertAPIView


router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))

]
