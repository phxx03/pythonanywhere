from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index),
	path('myweb/', include('myweb.urls')),
	path('polls/', include('polls.urls')),
	#path('united', views.united),
	path('admin/', admin.site.urls),
    path('Login', views.Login),
    path('logout', views.logout),
    path('Register', views.Register),
    path('indexuser', views.indexuser),
    path('Write', views.Write),
]
