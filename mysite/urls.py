from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
	path('', views.index),
	path('myweb/', include('myweb.urls')),
	path('polls/', include('polls.urls')),
	#path('united', views.united),
	path('admin/', admin.site.urls),
]
