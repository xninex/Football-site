from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:new_id>/', views.detail, name='detail'),
    path('<int:new_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]