from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('candidate/', include('candidate.urls')),
    path('', include('Jobs.urls')),


    path('lead/', include('Leads.urls')),
    


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

