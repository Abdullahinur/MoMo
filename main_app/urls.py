from django.conf.urls import url

# import view functions
from . import views

# The url patterns:
urlpatterns = [
    url(r'', views.main, name='main')
]
