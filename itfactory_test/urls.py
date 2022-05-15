from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from tp_visit.views import VisitCreateView
from trade_point.views import TradePointListView

schema_view = get_schema_view(
    openapi.Info(
        title="IT Factory Test Task API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('list/<int:phone_number>/', TradePointListView.as_view()),
    path('post/<int:phone_number>/', VisitCreateView.as_view())
]
