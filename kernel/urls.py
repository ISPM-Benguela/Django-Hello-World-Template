from django.conf.urls import url, include
from django.contrib import admin


from kernel import views as visao

urlpatterns = [
    url(r'^$', visao.inicio, name='inicio'),
]
