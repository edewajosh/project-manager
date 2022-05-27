
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
                TokenObtainPairView,
                TokenRefreshView,
                TokenVerifyView,
            )

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Agile Project",
      default_version='v1',
      description="Agile Project Management Tool",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="joshuaedewa@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('user.urls')),

     # simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
   # django debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

    # swagger drf_yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# silk url
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]