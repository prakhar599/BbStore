from xml.etree.ElementInclude import include
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('createnew',views.create_Blog,name="create_blog"),
    path('updateblog',views.update_Blog,name="update_blog"),
    path('readblog/<int:myid>/',views.read_Blog,name="readblog"),
    path('aboutus',views.about_Us,name="about_us"),
    path('login/',views.logIn,name="logIn"),
    path('logout/',views.logout,name="logOut"),
    path('signup/',views.signUp,name="signUp"),
    path('books',views.books,name='books'),
    path('contact/', views.contact, name='contact'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)