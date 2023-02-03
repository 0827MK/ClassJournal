from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib import admin

app_name='employee'

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>/',  views.DetailView.as_view(), name='detail'),]