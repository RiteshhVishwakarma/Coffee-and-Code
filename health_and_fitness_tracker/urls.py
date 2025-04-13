from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tracker.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Static files serve karne ke liye (only for local testing when DEBUG=False)
# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

# http://127.0.0.1:8000/staticfiles/css/index.css