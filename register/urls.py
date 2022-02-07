from django.urls import path,include
from . import views
from django.views.generic import TemplateView

app_name='register'

urlpatterns = [
  # path('', views.home, name='registration'),
  path('', views.Renderform, name="form-view"),
  path('success/', views.success, name="success-page"),
  # path('handlepayment/', views.handlepayment, name="handlepayment"),
  path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
