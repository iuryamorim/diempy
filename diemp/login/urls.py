from django.conf.urls import url

from diemp.aluno.views import new, call_logout, import_csv

urlpatterns = [
    url(r'^$', new, name='login'),
    url(r'^logout/$', call_logout),
    url(r'^(\w+)/$', import_csv, name='import'),
]