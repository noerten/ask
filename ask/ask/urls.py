from django.conf.urls import url
from django.contrib import admin
from qa import views
                                                        
urlpatterns = [
   url(r'^$', views.main_page),
   url(r'^admin/', admin.site.urls),
   url(r'^login/.*$', views.test, name='login'),
   url(r'^signup/.*', views.test, name='signup'),
   url(r'^question/(?P<id>[0-9]+)/$', views.questions, name='question'),
   url(r'^ask/.*', views.test, name='ask'),
   url(r'^popular/.*', views.popular, name='popular'),
   url(r'^new/.*', views.test, name='new'),
]
