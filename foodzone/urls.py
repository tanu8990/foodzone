
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact/',views.contact_us,name="contact"),
    path('booking',views.booking,name="booking"),
    path('menu',views.menu,name="menu"),
    path('menu/category/<int:id>',views.getProduct, name='getProduct'),
    path('single',views.single,name="single")
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
