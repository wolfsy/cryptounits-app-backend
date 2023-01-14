from django.urls import re_path
from App import views 


urlpatterns = [
    re_path(r'^wallets$', views.wallet_list),
    re_path(r'^wallet/(?P<id>[0-9]+)$', views.wallet_detail)
]