from django.urls import path
from .views import VideoListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)