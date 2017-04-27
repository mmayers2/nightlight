from django.conf.urls import url
from . import views

app_name = 'listings'

urlpatterns = [
    # /listings/
    url(r'^$', views.IndexView, name='index'),

    # /listings/<listing_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
