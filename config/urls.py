# from django.contrib import admin
# from django.urls import path, include
#
# from django.urls import re_path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# # from django.views.generic import TemplateView
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Online Manufacturing API",
#       default_version='v1',
#       description="API for Online Product, Material, ProductMaterial and Warehouse  app",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="usmonovakobir82@gmail.com "),
#       license=openapi.License(name="No licence"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/auth/', include('rest_framework.urls')),
#     path('api/manufactur/', include('manufactur.urls')),
#     path('product/', include('manufactur.urls')),
# #   For API documentation
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Online Manufacturing API",
        default_version='v1',
        description="API for Online Product, Material, ProductMaterial and Warehouse app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="usmonovakobir82@gmail.com"),
        license=openapi.License(name="No licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/manufactur/', include('manufactur.urls')),
    path('product/', include('manufactur.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
