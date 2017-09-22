from django.conf.urls import url
from . import views #get current dir views

urlpatterns = [
    #/cards/
    url(r'^$', views.index, name='index'),

    #/cards/add
    url(r'^add/$', views.CardCreate.as_view(), name='card-add'),

    #/cards/2/
    url(r'(?P<pk>[0-9]+)/$', views.CardUpdate.as_view(), name='card-update'),

]