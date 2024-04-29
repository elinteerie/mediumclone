
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(openapi.Info(
    title="Medium Clone",
    default_version="v0.1", 
    description="API endpoint for Medium Clone",
    contact=openapi.Contact(email="elinteerie@gmail.com"),
    license=openapi.License(name="MIT License")


),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]


admin.site.site_header = "Medium Clone"
admin.site.site_title = "Medium Clone Admin Portal"

admin.site.index_title = "Welcome to Medium CLone"
