from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home,name = 'home'),
    url(r'^neighborhood/', views.neighborhood, name='neighborhood'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_neighborhood,name = 'past_days_neighborhood'),
]