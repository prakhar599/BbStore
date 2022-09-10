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
    path('contact',views.contact_Us,name="contact_us"),
    path('aboutus',views.about_Us,name="about_us"),
    path('login/',views.logIn,name="logIn"),
    path('signup/',views.signUp,name="signUp"), 
    path('books',views.books,name='books'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)    