from django.conf.urls import url

# Import views from the main app
from . import views

# URL PATTERNS
urlpatterns = [
    url(r'', views.main, name='main')
]
