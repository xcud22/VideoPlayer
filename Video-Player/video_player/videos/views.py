from django.views.generic.list import ListView
from .models import Video

class VideoListView(ListView):
    model = Video
    template_name = 'video_list.html'