from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

from core import views
from sistema import settings

urlpatterns = [
                  path('accounts/login/', views.LoginView.as_view(), name='login'),
                  path('admin/', admin.site.urls),
                  path('', include('core.urls')),

                  path('api_rest/', include('api_rest.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
