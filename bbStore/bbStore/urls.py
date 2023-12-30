from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import UserViewSet
from django.shortcuts import redirect


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'userapi', views.UserViewSet)
router.register('blogapi',views.BlogViewSet)

def redirect_to_blog(request):
    return redirect('/blog/')

urlpatterns = [
     path('admin/', admin.site.urls),
     path('blog/',include('blog.urls')),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('api/', include(router.urls)),
     path('', redirect_to_blog),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
