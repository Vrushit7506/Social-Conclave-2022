from django.urls import path,include
from . import views
from django.views.generic import TemplateView

app_name='register'

urlpatterns = [
  # path('', views.home, name='registration'),
  path('', views.Renderform, name="form-view"),
]
