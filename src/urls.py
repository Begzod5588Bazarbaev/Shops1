from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from app.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/success', TemplateView.as_view(template_name='registration/success.html'), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('posts/', include('app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)