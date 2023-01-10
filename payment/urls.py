from django.urls import path, re_path
from .views import payment, PaymentCreateView, success

urlpatterns = [
    path('<int:link_id>/success.html', success),
    path('<int:link_id>/', PaymentCreateView.as_view()),
    #path('<int:link_id>/', payment),
]
