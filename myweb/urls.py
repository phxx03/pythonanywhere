from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # ex: /myweb/
    path('', views.index, name='index'),
    # ex: /myweb/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myweb/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myweb/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('',views.Register, name="Register"),
    path('',views.Login, name="Login"),
    path('',views.indexuser, name="indexuser"),
    path('',views.Write, name="Write"),
]