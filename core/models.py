from django.db import models
from django.core.validators import FileExtensionValidator
class Document(models.Model):

    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['wav','mp3','ogg'])])