from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
#     url('', views.index, name='index'),
    url('ranking/', views.ranking, name='ranking'),
    url('perfil/(?P<guerreiroId>\d+)', views.perfil)
#    url('dbz/grade', views.grade, name='grade'),
]
