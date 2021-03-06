from django.conf.urls import url, include
from rest_framework import routers

from api_rest.views import UserViewSet, LinkViewSet, LoginCreateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'links', LinkViewSet)
app_name = 'api_rest'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/',LoginCreateView.as_view(),name='login'),
]