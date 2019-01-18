from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/exists$', views.UserExistsView.as_view(), name='user-exists')
]
