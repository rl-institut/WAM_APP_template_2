from django.urls import path
from . import views
app_name = 'WAM_APP_template_2'

urlpatterns = [
    path('', views.example_view, name='index')
]
