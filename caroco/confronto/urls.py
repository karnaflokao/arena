from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url('', views.index, name='index'),
    # ex: /polls/5/
    url('<int:confronto_id>/', views.detail, name='detail'),
]