import imp
from django.conf.urls import url 
from template_app import views

# Template tagging 
app_name = 'template_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'), 
]