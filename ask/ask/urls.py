from django.conf.urls import url
from django.contrib import admin
from qa import views
                                                        
urlpatterns = [
   url(r'^$', views.main_page),
   url(r'^admin/', admin.site.urls),
   url(r'^login/.*$', views.test, name='login'),
   url(r'^signup/.*', views.test, name='signup'),
   url(r'^question/(?P<question_id>[0-9]+)/$', views.questions, name='question'),
   url(r'^ask/.*', views.question_add, name='ask'),
   url(r'^popular/.*', views.popular, name='popular'),
   url(r'^new/.*', views.test, name='new'),
   url(r'^answer/', views.answer_add, name='answer_add')
]
