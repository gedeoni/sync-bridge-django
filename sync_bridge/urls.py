from django.contrib import admin
from django.urls import include, path
from graphql_api.views import graphql_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('health.urls')),
    path('api/v1/', include('sync.urls')),
    path('api/v1/', include('sync_history.urls')),
    path('graphql', graphql_view, name='graphql'),
]
