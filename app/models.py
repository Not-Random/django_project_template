from django.db import models
from pathlib import Path

# you can find more details on Django models here: 
#   https://docs.djangoproject.com/en/4.1/topics/db/models/

class UploadedFile(models.Model):
    """ Uploads the file into the 'upload_path'
    """
    
    # creates the upload path if it does not exist
    upload_path = Path("volumes/media_root/uploads/")
    if not upload_path.exists():
        upload_path.mkdir(parents=True, exist_ok=True)

    # uploads file to 'upload_path'
    file = models.FileField(upload_to = upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name