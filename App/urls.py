from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from App import views 

schema_view = get_schema_view(
   openapi.Info(
      title = "Snippets API",
      default_version = 'v1',
      description = "Test description",
      terms_of_service = "https://www.google.com/policies/terms/",
      contact=openapi.Contact(email = "contact@snippets.local"),
      license=openapi.License(name = "BSD License"),
   ),
   public = True,
   permission_classes = [permissions.AllowAny],
)

urlpatterns = [
   re_path(r'^wallets$', views.wallet_list),
   re_path(r'^wallet/(?P<id>[0-9]+)$', views.wallet_detail),
   re_path(r'^cryptos$', views.crypto_list),
   re_path(r'^register$', views.register_user),
   re_path(r'^login$', views.login_user),
   re_path(r'^users$', views.user_list),
   re_path(r'^user$', views.user_view),
   re_path(r'^logout$', views.logout_user),
   re_path(r'^transaction$', views.perform_transaction),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]