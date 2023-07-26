from django.urls import path
from .views import IndexView
from django.views.decorators.cache import cache_page
app_name = 'coreapp'

urlpatterns = [
    path('', cache_page(timeout=60*120, key_prefix='index')(IndexView.as_view()), name='index'),
]
