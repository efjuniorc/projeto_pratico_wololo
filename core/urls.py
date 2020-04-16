from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from sistema import settings
from . import views

app_name = 'core'
urlpatterns = [
                  path('', views.testa_user_logado, name='login2'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('logout/', views.LogoutRedirectViews.as_view(), name='logout'),
                  path('dashboard/', views.Dashboard.as_view(), name='index'),
                  path('links_create_view/', views.LinkCreateView.as_view(), name='links_create_view'),
                  path('links_update_view/<int:pk>', views.LinkUpdateView.as_view(), name='links_update_view'),
                  path('links_delete_view/<int:pk>', views.LinkDeleteView.as_view(), name='links_delete_view'),
                  path('<str:url>', views.RedirectLink.as_view(), name='redirect_link'),
              ] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
