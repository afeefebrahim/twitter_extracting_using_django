from django.conf.urls import include, url
from . import views

urlpatterns =[
    url(r'^$',views.index,name = 'index'),
    url(r'^update/(?P<pk>[0-9]+)',views.update,name ='update'),
    url(r'^show/(?P<pk>[0-9]+)',views.show,name = 'show'),
    url(r'^new_id/$',views.new_id,name = 'new_id')
]