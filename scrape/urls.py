from django.urls import path

from . import views

app_name = 'scrape'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:page_id>/', views.detail , name='detail')
]