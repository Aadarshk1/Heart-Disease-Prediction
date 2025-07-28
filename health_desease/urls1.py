from django.contrib import admin
from django.urls import path, include
from devicetoserver import urls as devicetoserver_urls # type: ignore
from accounts.views import user_login, edit # type: ignore
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .api import router
from .apirep import routerep
from allauth.account.views import confirm_email # type: ignore

urlpatterns = [
    # Admin URLs
    path('admin/filebrowser/', include('filebrowser.urls')),
    path('admin/log_viewer/', include('log_viewer.urls')),
    path('admin/', admin.site.urls),
    
    # Application URLs
    path('', include(devicetoserver_urls)),  # Include devicetoserver app URLs
    path('accounts/', include('accounts.urls')),
    path('modelselection/', include('modelselection.urls')),
    path('computervision/', include('computervision.urls')),
    path('report/', include('fesibility.urls')),
    path('supportsystem/', include('supportsystem.urls')),
    path('openvino/', include('openvinofreezed.urls')),
    path('softwareactivation/', include('softwareactivation.urls')),
    path('instancesegmentation/', include('instancesegmentation.urls')),
    path('sensovisionshop/', include('ecommerce_app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('inventory/', include('inventory.urls')),
    path('salerecord/', include('salesapp.urls')),

    # API Endpoints
    path('api/sensoviz/', include(router.urls)),
    path('api/v1/', include(routerep.urls)),

    # REST Authentication
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # Allauth and Email Confirmation
    path('accounts-rest/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
    path('allaccounts/', include('allauth.urls')),

    # HR and Accounting URLs
    path('hr/', include('hiring.urls')),
    path('account/', include('accountant.urls', namespace='account')),

    # Analytics and Text Editors
    path('analytics/', include('analytics.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Orders
    path('orders/', include('orders.urls')),
]

# Static and media files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin site customization
admin.site.site_header = "Sensovision"
admin.site.site_title = "Sensovision Portal"
admin.site.index_title = "Welcome to Sensovision"
