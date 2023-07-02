from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


swagger_view = get_schema_view(
    openapi.Info(
        title="Virtual Queue",
        default_version="v1"
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('queues.urls')),

    re_path(
        r'^docs/$',
        swagger_view.with_ui("swagger", cache_timeout=0),
        name='api-docs'
    )
]
