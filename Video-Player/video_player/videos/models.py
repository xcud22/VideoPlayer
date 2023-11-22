from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Video(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=100)
	video_file = models.FileField(upload_to='uploads/video_files', validators = [FileExtensionValidator(allowed_extensions=['mp4', 'mpeg4', 'mpeg'])])
	date_created = models.DateTimeField(default=timezone.now)