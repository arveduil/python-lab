from django.conf.urls import url

from . import views

# 3 Add a namespace so Django knows what directory to load
# if another app has views with the same name
app_name = 'polls'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^/add_question/$', views.add_question, name='add_question'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/add_choice/$', views.add_choice, name='add_choice'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
