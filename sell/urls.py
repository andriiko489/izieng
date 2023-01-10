from django.urls import path
from .views import link
urlpatterns = [
    path('<int:link_id>/', link),
]
