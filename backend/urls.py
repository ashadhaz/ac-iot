from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^data/(?P<sdate>(\d{4}-\d{2}-\d{2}))/(?P<edate>(\d{4}-\d{2}-\d{2}))/$', views.get_data, name='index'),
    url(r'^add_data', views.add_data, name='add_data'),
]