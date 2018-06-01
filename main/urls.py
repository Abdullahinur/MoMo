from django.conf.urls import url
from django.contrib.auth import views as auth_views

# Import views from the main app
from . import views

# URL PATTERNS
urlpatterns = [
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^register/', views.register, name='register'),
    url(r'', views.main, name='main'),
]
